import os
from src.utils import write_response
import requests

headers = {
    "Host": "b.i.instagram.com",
    "Accept-Language": "en-US",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Ig-Intended-User-Id": "0",
    "Priority": "u=3",
    "X-Bloks-Is-Layout-Rtl": "false",
    "X-Bloks-Prism-Button-Version": "CONTROL",
    "X-Bloks-Prism-Colors-Enabled": "false",
    "X-Bloks-Prism-Extended-Palette-Gray": "false",
    "X-Bloks-Prism-Extended-Palette-Indigo": "false",
    "X-Bloks-Prism-Extended-Palette-Polish-Enabled": "false",
    "X-Bloks-Prism-Extended-Palette-Red": "false",
    "X-Bloks-Prism-Extended-Palette-Rest-Of-Colors": "false",
    "X-Bloks-Prism-Font-Enabled": "false",
    "X-Bloks-Prism-Indigo-Link-Version": "0",
    "X-Bloks-Version-Id": "b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Connection-Type": "WIFI",
    "X-Fb-Friendly-Name": "IgApi: attestation/create_android_keystore/",
    "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"567067343352427","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
    "X-Fb-Server-Cluster": "True",
    "X-Ig-Android-Id": "android-f35f126bc4795e76",
    "X-Ig-App-Id": "567067343352427",
    "X-Ig-App-Locale": "en_US",
    "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
    "X-Ig-Bandwidth-Totalbytes-B": "0",
    "X-Ig-Bandwidth-Totaltime-Ms": "0",
    "X-Ig-Client-Endpoint": "unknown",
    "X-Ig-Capabilities": "3brTv10=",
    "X-Ig-Connection-Type": "WIFI",
    "X-Ig-Device-Id": "941b3b2b-4663-46cc-bf7a-5e6da6c68528",
    "X-Ig-Device-Locale": "en_US",
    "X-Ig-Is-Foldable": "true",
    "X-Ig-Mapped-Locale": "en_US",
    "X-Ig-Timezone-Offset": "7200",
    "X-Ig-Www-Claim": "0",
    "X-Pigeon-Rawclienttime": "1768752933.577",
    "X-Pigeon-Session-Id": "UFS-107db36b-e0f0-4f5e-8bb0-5506d103b806-0",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '67',
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Fb-Conn-Uuid-Client": "54cb3412e733a34fd05f0353ea3872ea",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
}

data = {
    "app_scoped_device_id": "941b3b2b-4663-46cc-bf7a-5e6da6c68528",
    "key_hash": "",
}

response = requests.post(
    "https://b.i.instagram.com/api/v1/attestation/create_android_keystore/",
    headers=headers,
    data=data,
    verify=False,
)

write_response(response, os.path.dirname(__file__))
