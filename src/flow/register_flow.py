import asyncio


import os
import json
import random
from datetime import datetime

from src.flow import utils
from src.flow.schemas import EmailAccount
from mail import fetch_latest_message

_FIRST_NAMES = (
    "Liam",
    "Noah",
    "Oliver",
    "Elijah",
    "James",
    "William",
    "Benjamin",
    "Lucas",
    "Henry",
    "Alexander",
    "Olivia",
    "Emma",
    "Ava",
    "Sophia",
    "Isabella",
    "Mia",
    "Charlotte",
    "Amelia",
    "Evelyn",
    "Abigail",
)

_LAST_NAMES = (
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
)


def get_account_from_file() -> EmailAccount:
    folder = "./emails"
    files = [f for f in os.listdir(folder) if f.endswith(".txt")]

    random_file = random.choice(files)
    filepath = os.path.join(folder, random_file)

    with open(filepath, "r") as f:
        data = json.load(f)

    return EmailAccount(**random.choice(data))


async def main():
    # flow = Flow("ringoo172014@gmail.com", "vitaliiLutsyk18112005@Instagram")
    # response = await flow.login_flow()

    # payload = {
    #     "url": response.url,
    #     "status": response.status.as_int(),
    #     "json": response.json,
    #     "text": None,
    # }
    # response_json = await response.json()
    # try:
    #     payload["json"] = response_json
    # except ValueError:
    #     payload["text"] = response.text

    # with open("out_path.json", "w", encoding="utf-8") as f:
    #     json.dump(payload, f, ensure_ascii=False, indent=2)

    # print(response)

    from src.flow.registration import RegistrationFlow
    from src.schema import RegData

    email_account = get_account_from_file()

    current_year = datetime.now().year
    birth_date = utils.generate_birth_date(current_year - 35, current_year - 19)

    some: RegData = RegData(
        email=email_account.email,
        password=email_account.password + "@Instagram",
        refresh_token=email_account.refresh_token,
        email_client_id=email_account.client_id,
        name=f"{random.choice(_FIRST_NAMES)}",
        username=email_account.email.split("@")[0],
        birth_date=birth_date,
    )

    some: RegistrationFlow = RegistrationFlow(some)

    response = await some.run()
    response_json = await response.json()

    print(response_json)
    print(response_json)


if __name__ == "__main__":
    asyncio.run(main())
