# pip install gmqtt (if allowed; it's lightweight)

import asyncio
import gmqtt
import base64
import json
import secrets


async def on_connect(client, flags, rc, properties):
    print("Connected, RC:", rc)
    await client.subscribe("/fbns_reg_resp", qos=1)


async def on_message(client, topic, payload: bytes, qos, properties):
    print(f"Topic: {topic}")
    try:
        # Payload is often zipped Thrift → try decompress
        import zlib

        decompressed = zlib.decompress(payload)
    except:
        decompressed = payload

    # Look for base64 patterns (device_token.k is base64 JSON)
    payload_str = decompressed.decode("utf-8", errors="ignore")
    print("Payload snippet:", payload_str[:500])  # Debug

    # Heuristic: find eyJ... (base64 start for JSON)
    if "eyJ" in payload_str:
        # Crude extract – improve with regex if needed
        start = payload_str.find("eyJ")
        end = payload_str.find('"', start + 100)
        candidate = payload_str[start:end]
        try:
            decoded = base64.b64decode(candidate + "==").decode()  # Padding fix
            print("Possible device_token.k base64:", candidate)
            print("Decoded inner:", decoded)
            # Build device_token as above
        except:
            pass


async def main():
    client = gmqtt.Client(client_id="android-" + secrets.token_hex(8))
    # Meta uses weird username/password for auth – from captures: often username=your_ig_user_id or device_token-like
    # You may need to sniff real CONNECT username/password from Burp first
    # Placeholder – replace with real from capture
    await client.connect("mqtt-ig-p4.facebook.com", 443, ssl=True)

    client.on_connect = on_connect
    client.on_message = on_message

    # Keep running
    await asyncio.sleep(3600)  # 1 hour


asyncio.run(main())
