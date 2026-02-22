from pydantic import BaseModel


class BasicData(BaseModel):
    android_id: str
    family_device_id: str
    waterfall_id: str
    device_id: str
    app_id: str
    bloks_version: str
    user_agent: str
    aacjid: str
    user_agent: str


class RegistrationData(BasicData):
    experiment_group: str
    registration_flow_id: str
    email: str
    encrypted_password: str
    raw_password: str
    name: str
    username: str
    confirmation_code: str | None = None
    data_encryption_key_id: int
    data_encryption_key: str
    birth_date: str
    qpl_instance_id: list[float]
    qpl_marker_id: int
    safetynet_token: str  # add this on password creation response

    zero_eh: (
        str  # same for unauthorized users "IG0e09d776530888418ab70f3822fbb4e1"
    )
    event_request_id: list[str]


class RegData(BaseModel):
    email: str
    password: str
    refresh_token: str
    email_client_id: str
    name: str
    username: str
    confirmation_code: str | None = None
    birth_date: str
    safetynet_token: str | None = None


class EmailResponse(BaseModel):
    code: str | None
    date: str | None
