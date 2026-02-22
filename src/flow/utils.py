from datetime import datetime
import struct
import uuid
import random
import string
import hashlib

import base64

from Cryptodome import Random
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA

import re
import json

from src.flow.schemas import InputIds, RegistrationDict
from src.flow.user_agent import user_agents
import hmac
from time import timezone
from src.flow.schemas import BloksPayloadType


def generate_uuid() -> str:
    return str(uuid.uuid4())


def create_pigeon_session_id() -> str:
    return f"UFS-{uuid.uuid4()}-0"


def get_pigeon_raw_client_time() -> str:
    return f"{datetime.now().timestamp():.3f}"


def generate_android_id(username) -> str:
    return f"android-{''.join(random.choices(string.hexdigits.lower(), k=16))}"


def generate_family_device_id(username: str) -> str:
    digest = hashlib.sha256(("family" + username).encode()).hexdigest()
    return f"{digest[:8]}-{digest[8:12]}-{digest[12:16]}-{digest[16:20]}-{digest[20:32]}"


def generate_mid() -> str:
    return str(uuid.uuid4())


def generate_waterfall_id() -> str:
    """
    6c79c9de-55cc-4404-99d9-a88591831e9e
    """
    return str(uuid.uuid4())


def get_user_agent() -> str:
    return random.choice(user_agents)


def generate_ig_device_id(username: str) -> str:
    hash_object = hashlib.sha256(username.encode())
    hex_dig = hash_object.hexdigest()
    return f"{hex_dig[:8]}-{hex_dig[8:12]}-{hex_dig[12:16]}-{hex_dig[16:20]}-{hex_dig[20:32]}"


def encrypt_password(
    raw_client_time: int | None,
    key_id: int,
    pub_key: str,
    raw_password: str,
) -> str:
    if not raw_client_time:
        raw_client_time = get_pigeon_raw_client_time()

    key = Random.get_random_bytes(32)
    iv = Random.get_random_bytes(12)
    print(pub_key)
    pubkey = base64.b64decode(pub_key)

    rsa_key = RSA.importKey(pubkey)
    rsa_cipher = PKCS1_v1_5.new(rsa_key)
    encrypted_key = rsa_cipher.encrypt(key)

    aes = AES.new(key, AES.MODE_GCM, nonce=iv)
    aes.update(str(raw_client_time).encode("utf-8"))

    encrypted_password, cipher_tag = aes.encrypt_and_digest(
        bytes(raw_password, "utf-8")
    )

    encrypted = bytes(
        [
            1,
            key_id,
            *list(iv),
            *list(struct.pack("<h", len(encrypted_key))),
            *list(encrypted_key),
            *list(cipher_tag),
            *list(encrypted_password),
        ]
    )

    encrypted = base64.b64encode(encrypted).decode("utf-8")
    return f"#PWD_INSTAGRAM:4:{raw_client_time}:{encrypted}"


def get_aacjid(initial_lispy: str) -> str:
    json_str = re.search(r"\{.*\}", initial_lispy).group(0).replace('\\"', '"')
    data = json.loads(json_str)

    return data["aacjid"]

def get_aac_init_timestamp(initial_lispy: str) -> int:
    json_str = re.search(r"\{.*\}", initial_lispy).group(0).replace('\\"', '"')
    data = json.loads(json_str)
    print(data)

    return int(data["aac_init_timestamp"])


def get_input_ids(text: str) -> InputIds:
    m = re.search(
        r'"password"\s+"([A-Za-z_][A-Za-z0-9_]*:\d+)"\s+"([A-Za-z_][A-Za-z0-9_]*:\d+)"',
        text,
    )

    print(m)
    if m:
        full1, full2 = m.group(1), m.group(2)
        return InputIds(username_id=full2, password_id=full1)
    return None, None


def generate_password(username: str) -> str:
    hash_object = hashlib.sha256((username + "!@#$%^&*()_+").encode())
    hex_dig = hash_object.hexdigest()
    return f"{hex_dig[:8]}-{hex_dig[8:12]}-{hex_dig[12:16]}-{hex_dig[16:20]}-{hex_dig[20:32]}"


def generate_birth_date(start_year: int, end_year: int) -> str:
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)
    return f"{day:02d}-{month:02d}-{year}"


def get_qpl_ids(text: str) -> tuple[int, float]:
    pattern = re.compile(
        r'(\d+)\s+(\d+)\s+"com\.bloks\.www\.bloks\.caa\.login\.async\.send_login_request"'
    )
    m = pattern.search(text)
    if m:
        id1, id2 = m.groups()
        return int(id1), float(id2)


def get_qpl_instance_id(text: str) -> float:
    return get_qpl_ids(text)[1]


def get_qpl_marker_id(text: str) -> int:
    return get_qpl_ids(text)[0]


def extract_event_id(text: str) -> str:
    pass



def safetynet_token(email: str, timestamp: int) -> str:
    payload = f"{email}|{timestamp}".encode()

    secret = b"yfN2vDub_GLtgJAZLHmDdksZG_UlyYoHjLOplQUUFA"  ### dummy secret

    sig = hmac.new(secret, payload, hashlib.sha256).digest()[:24]
    token = base64.b64encode(payload + b"|" + sig).decode()

    return token


def date_to_unix_timestamp(date_str: str) -> int:
    dt = datetime.strptime(date_str, "%d-%m-%Y")
    return int(dt.replace(tzinfo=timezone.utc).timestamp())


def __bloks_payload(data: dict, bloks_type: BloksPayloadType) -> dict:
    if bloks_type == BloksPayloadType.APP:
        return data["data"][
            f"1$bloks_{bloks_type.value}(bk_context:$bk_context,params:$params)"
        ]["screen_content"]["component"]["bundle"]
    else:
        return data["data"][
            f"1$bloks_{bloks_type.value}(bk_context:$bk_context,params:$params)"
        ]["action"]["action_bundle"]


def __find_reg_info(layout: dict) -> None:
    first_entry = str(layout).find("first_name")
    last_entry = str(layout).find("}", first_entry)

    reg_info = str(layout)[first_entry - 5 : last_entry + 2]
    return reg_info


def get_registration_dictionary(
    response: dict, bloks_type: BloksPayloadType = BloksPayloadType.ACTION
) -> RegistrationDict:
    bl_pl = __bloks_payload(response, bloks_type)
    if bloks_type == BloksPayloadType.ACTION:
        layout = json.loads(bl_pl["bloks_bundle_action"])["layout"]
    else:
        layout = json.loads(bl_pl["bloks_bundle_tree"])["layout"]
    reg_info_str = str(__find_reg_info(layout)).replace('\\"', '"')
    reg_info = json.loads(reg_info_str)
    return reg_info


def get_registration_context_token(
    response: dict, bloks_type: BloksPayloadType = BloksPayloadType.ACTION
) -> list[str]:
    bl_pl = __bloks_payload(response, bloks_type)

    if bloks_type == BloksPayloadType.ACTION:
        layout = json.loads(bl_pl["bloks_bundle_action"])["layout"]
    else:
        layout = json.loads(bl_pl["bloks_bundle_tree"])["layout"]

    layout_str = json.dumps(layout, ensure_ascii=False).replace('\\"', '"')

    matches = re.findall(r'[^"]*\|regm', layout_str)

    if matches:
        return matches[-1]


def find_reg_inputs(text: str):
    numbers = re.findall(r"\(eud (\d+)\)", text)
    numbers = [x for x in numbers if x != "0"]
    return numbers


def find_availiable_usernames(text: str, username: str) -> list[str]:
    pattern = rf"\\\"({username}[a-zA-Z0-9._]+)\\\""
    return re.findall(pattern, text)


def find_email_input_id(text: str) -> str:
    match = re.findall(
        r"(eud (\d+))",
        text,
    )
    input_id = [x for x in match if x[1] != "0"]
    print(input_id)
    return input_id[0][1]


def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def get_confirmation_code_input_id(
    text: str, position: int = 1
) -> tuple[str, int]:
    pattern = r'\(dkc\s*\\?["\\]*([^"\\]+)["\\]*[^)]*\(eud\s*(\d+)'
    matches = re.findall(pattern, text, re.DOTALL)

    if not matches:
        raise ValueError("No matches found")

    event_id, input_id = remove_duplicates(matches)[position]
    return event_id, int(input_id)


def get_qpl_for_confirmation_code(text: str) -> tuple[float]:
    pattern = r'(\d+)\s*(?:\\+)?\"com\.bloks\.www\.bloks\.caa\.reg\.confirmation\.async'

    match = re.findall(pattern, text)
    if match:
        number = match[-1]  
        return float(number)
    else:
        print("No match")

