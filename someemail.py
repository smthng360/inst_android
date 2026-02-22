import asyncio
from email import message_from_bytes
from email.header import decode_header, make_header
from email.utils import parseaddr

import aiohttp
from aioimaplib import aioimaplib


async def get_access_token(
    session: aiohttp.ClientSession,
    client_id: str,
    refresh_token: str,
) -> str:
    form = {
        "client_id": client_id,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "scope": "https://outlook.office.com/IMAP.AccessAsUser.All",
    }
    async with session.post(
        "https://login.microsoftonline.com/consumers/oauth2/v2.0/token",
        data=form,
    ) as r:
        body = await r.json()
        if "access_token" not in body:
            raise RuntimeError(body.get("error_description", body))
        return body["access_token"]


async def fetch_latest_message(
    email: str,
    client_id: str,
    refresh_token: str,
) -> str:
    async with aiohttp.ClientSession() as session:
        access_token = await get_access_token(
            session=session,
            client_id=client_id,
            refresh_token=refresh_token,
        )

    imap = aioimaplib.IMAP4_SSL(host="outlook.office365.com", port=993)

    assert imap.protocol is not None
    await imap.wait_hello_from_server()

    await imap.xoauth2(user=email, token=access_token)  # type: ignore[reportArgumentType]
    await imap.select("INBOX")
    status, (ids_bytes, _) = await imap.search("ALL", charset="US-ASCII")

    if status != "OK" or not ids_bytes:
        return "inbox empty"

    latest = ids_bytes.split()[-1].decode()
    status, msg_parts = await imap.fetch(latest, "(RFC822)")
    raw_msg = msg_parts[1]
    await imap.logout()

    # Parse headers
    msg = message_from_bytes(raw_msg)
    # print(msg)
    subj = str(make_header(decode_header(msg["Subject"] or "")))
    name, addr = parseaddr(msg["From"] or "")
    date = msg["Date"]
    return f"Newest mail: {subj} | {name or addr} | {date}"


if __name__ == "__main__":
    CREDS = {
        "Email": "email",
        "Password": "password",
        "RefreshToken": "refresh_token",
        "AccessToken": None,
        "R_Expire": "r_expire",
        "ClientId": "client_id",
    }

    email = asyncio.run(
        fetch_latest_message(
            email=CREDS["Email"],
            client_id=CREDS["ClientId"],
            refresh_token=CREDS["RefreshToken"],
        )
    )
    print(email)
