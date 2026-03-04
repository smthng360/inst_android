import asyncio
from email import message_from_bytes
from email.header import decode_header, make_header
from email.utils import parseaddr
import re
from src.schema import EmailResponse

from datetime import datetime, timezone
import aiohttp
from aioimaplib import aioimaplib


def comparate_date(date_str: str, submission_time: datetime) -> bool:
    date_str = re.sub(r"\s*\(.*?\)\s*$", "", date_str).strip()
    parsed_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")

    submission_time = submission_time.astimezone(parsed_date.tzinfo)

    print(parsed_date)
    print(submission_time)
    return parsed_date >= submission_time


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
    submission_time: datetime,
) -> EmailResponse:
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

    msg = message_from_bytes(raw_msg)

    subj = str(make_header(decode_header(msg["Subject"] or "")))
    name, addr = parseaddr(msg["From"] or "")
    date = msg["Date"]
    print(f"Newest mail: {subj} | {name or addr} | {date}")

    if not comparate_date(date, submission_time):
        return None

    code = re.search(r"(\d{6})", subj)
    if code:
        return EmailResponse(code=code.group(1), date=date)
    return None


if __name__ == "__main__":
    CREDS = {
        "Email": "bomarqstutiapt@outlook.com",
        "Password": "uaY24zRCsjAj7x",
        "RefreshToken": "M.C557_BAY.0.U.-Ct3ci82BVn57QNpFOBbKrTqJj77uwqOBhUctkwkriPf1NiE1!E0i84wfe9ulO73KOERGoYNMI8yhfg80*IPkXKYBQFCq!F7E9Gd1NlCinbl2K2SP9K29Q22n2sXvkdlMqTIC8cy0nSlSlRmyhFjYf7xnY4Gfi9cFa1Ba4QWmDsWeW5WJLqHwSY!j4**LCqbRwxdFGk4YbYqbwFkxsPqVa3SCsSkZu6AsUa21*MjzplP9YCcl1CWFCBfTMwnQrjhUe!5dg1K1lRYNvHDzmCbCmnFi2oxCsmvDDawBEYntitF3mJ!csceNOkdNatgmQl8S1cmudjGR8OEG6KszKKm9ku1yKdlrEwHCh9L*1q1YX!SlOwct*Hm8ZwEQ90Yhb99FApaPdJ6csmbHnvGMPOMrxCmPt0xssuY9n3rXXpMHyk8r",
        "AccessToken": None,
        "R_Expire": "9e5f94bc-e8a4-4e73-b8be-63364c29d753",
        "ClientId": "9e5f94bc-e8a4-4e73-b8be-63364c29d753",
    }
    email = asyncio.run(
        fetch_latest_message(
            email=CREDS["Email"],
            client_id=CREDS["ClientId"],
            refresh_token=CREDS["RefreshToken"],
        )
    )
    print(email)
