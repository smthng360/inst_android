import os
from .consts import INSTAGRAM_VERSION, BLOKS_VERSION_ID, APP_ID
from . import utils
from . import body as body_import
from . import headers as headers_import
import requests
import json
from enum import StrEnum
import asyncio
from .schemas import InputIds
from rnet import Client, Emulation
from src.schema import RegistrationData, RegData
from rnet import Response


class Domains(StrEnum):
    binst: str = "https://b.i.instagram.com"
    zginst: str = "https://z-p42.graph.instagram.com"
    gfacebook: str = "https://graph.facebook.com"
    iinsragram: str = "https://i.instagram.com"


class Flow:
    def __init__(self, username: str, password: str) -> None:
        self._username: str = username
        self.email: str = None
        self._password: str = password
        self._device_id: str = utils.generate_ig_device_id(self._username)
        self._family_device_id: str = utils.generate_family_device_id(
            self._username
        )
        self._android_id: str = utils.generate_android_id(self._username)
        self._pigeon_session_id: str = utils.create_pigeon_session_id()
        self._mid: str = utils.generate_mid()
        self._log_seq: int = 0

        self._token: str = None

        self._encryption_pub_key: str | None = None
        self._encryption_key_id: int | None = None
        self._picked_instagram_version: str = INSTAGRAM_VERSION
        self._waterfall_id: str = utils.generate_waterfall_id()
        self._app_id: str = APP_ID
        self._blocks_version: str = BLOKS_VERSION_ID
        self._user_agent: str = utils.get_user_agent()

        self._aacjid: str = None

        self._key_nonce: str = None
        self._challenge_nonce: str = None

        self._input_ids: InputIds = None

        self._client = Client(
            emulation=Emulation.OkHttp3_14, user_agent=self._user_agent
        )

        self.qpl_instance_id: int = 0
        self.qpl_marker_id: float = 0.0

        self._experiment_group: str = "caa_iteration_v3_perf_ig_4"

        self.data: RegistrationData | None = None

        self._reg_context: str = None

    async def dual_token(self, is_stale: bool = False):
        headers = headers_import.get_dual_headers(
            device_id=self._device_id,
            user_agent=self._user_agent,
            blocks_version=self._blocks_version,
            android_id=self._android_id,
            pigeon_raw_client_time=utils.get_pigeon_raw_client_time(),
            pigeon_session_id=self._pigeon_session_id,
            app_id=self._app_id,
        )

        params_dict = {
            "is_from_logged_out": False,
            "logged_out_user": "",
            "qpl_join_id": utils.generate_uuid(),
            "family_device_id": None,
            "device_id": self._android_id,
            "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
            "waterfall_id": self._waterfall_id,
            "logout_source": "",
            "show_internal_settings": False,
            "last_auto_login_time": 0,
            "disable_auto_login": False,
            "qe_device_id": self._device_id,
            "use_auto_login_interstitial": True,
            "disable_recursive_auto_login_interstitial": True,
            "auto_login_interstitial_experiment_group_name": "",
            "is_from_logged_in_switcher": False,
            "switcher_logged_in_uid": "",
            "account_list": [],
            "blocked_uid": [],
            "INTERNAL_INFRA_THEME": "THREE_C",
            "layered_homepage_experiment_group": "ld_no_language_selector",
            "launched_url": "",
            "sim_phone_numbers": [],
            "is_from_registration_reminder": False,
        }

        data = {
            "params": json.dumps(params_dict),
            "bk_client_context": json.dumps(
                {
                    "bloks_version": self._blocks_version,
                    "styles_id": "instagram",
                }
            ),
            "bloks_versioning_id": self._blocks_version,
        }

        response = await self._client.post(
            url="https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.process_client_data_and_redirect/",
            headers=headers,
            data=data,
        )
        return response

    async def process_and_redirect(self):
        headers = headers_import.get_process_and_redirect_headers(
            device_id=self._device_id,
            user_agent=self._user_agent,
            x_mid=self._mid,
            app_id=self._app_id,
            blocks_version=self._blocks_version,
            android_id=self._android_id,
            pigeon_raw_client_time=utils.get_pigeon_raw_client_time(),
            pigeon_session_id=self._pigeon_session_id,
        )

        params_dict = {
            "is_from_logged_out": False,
            "logged_out_user": "",
            "qpl_join_id": utils.generate_uuid(),
            "family_device_id": None,
            "device_id": self._android_id,
            "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
            "waterfall_id": self._waterfall_id,
            "logout_source": "",
            "show_internal_settings": False,
            "last_auto_login_time": 0,
            "disable_auto_login": False,
            "qe_device_id": self._device_id,
            "use_auto_login_interstitial": True,
            "disable_recursive_auto_login_interstitial": True,
            "auto_login_interstitial_experiment_group_name": "",
            "is_from_logged_in_switcher": False,
            "switcher_logged_in_uid": "",
            "account_list": [],
            "blocked_uid": [],
            "INTERNAL_INFRA_THEME": "THREE_C",
            "layered_homepage_experiment_group": "ld_no_language_selector",
            "launched_url": "",
            "sim_phone_numbers": [],
            "is_from_registration_reminder": False,
        }

        data = {
            "params": json.dumps(params_dict),
            "bk_client_context": json.dumps(
                {
                    "bloks_version": self._blocks_version,
                    "styles_id": "instagram",
                }
            ),
            "bloks_versioning_id": self._blocks_version,
        }

        response = await self._client.post(
            url="https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.process_client_data_and_redirect/",
            headers=headers,
            form=data,
        )

        response_json = await response.json()

        if (
            "aacjid"
            in response_json["layout"]["bloks_payload"]["data"][-1]["data"][
                "initial_lispy"
            ]
        ):
            self._aacjid = utils.get_aacjid(
                response_json["layout"]["bloks_payload"]["data"][-1]["data"][
                    "initial_lispy"
                ]
            )

        ids = utils.get_input_ids(str(response_json["layout"]))

        self._input_ids = ids

        self._qpl_marker_id, self._qpl_instance_id = utils.get_qpl_ids(
            str(response_json["layout"]["bloks_payload"]["embedded_payloads"])
        )

        return response

    async def mobile_config(self):
        heads = headers_import.get_mobile_config_headers(
            device_id=self._device_id,
            user_agent=self._user_agent,
            app_id=self._app_id,
            blocks_version=self._blocks_version,
            android_id=self._android_id,
            pigeon_raw_client_time=utils.get_pigeon_raw_client_time(),
            pigeon_session_id=self._pigeon_session_id,
        )

        data = {
            "signed_body": "SIGNATURE."
            + json.dumps(
                {
                    "bool_opt_policy": "0",
                    "mobileconfigsessionless": "",
                    "api_version": "10",
                    "unit_type": "1",
                    "use_case": "STANDARD",
                    "query_hash": "3dda1251bd0edfd452095e7d3eb3c040f2513628cbded5de8031c732652ef7f6",
                    "tier": "-1",
                    "device_id": self._device_id,
                    "fetch_mode": "CONFIG_SYNC_ONLY",
                    "fetch_type": "SYNC_FULL",
                    "family_device_id": "EMPTY_FAMILY_DEVICE_ID",
                }
            ),
        }
        response = await self._client.post(
            url="https://b.i.instagram.com/api/v1/launcher/mobileconfig/",
            headers=heads,
            form=data,
        )
        self._mid = str(response.headers.get("ig-set-x-mid", None))
        self._encryption_pub_key = response.headers.get(
            "Ig-Set-Password-Encryption-Pub-Key", None
        )
        self._encryption_key_id = response.headers.get(
            "Ig-Set-Password-Encryption-Key-Id", None
        )

        return response

    async def token_fetch(self):
        heads = headers_import.get_token_fetch_headers(
            device_id=self._device_id,
            user_agent=self._user_agent,
            app_id=self._app_id,
            blocks_version=self._blocks_version,
            android_id=self._android_id,
            pigeon_raw_client_time=utils.get_pigeon_raw_client_time(),
            pigeon_session_id=self._pigeon_session_id,
            family_device_id=self._family_device_id,
            x_mid=self._mid,
        )
        if self._aacjid is None:
            self._aacjid = "b7b91a3d-4152-40be-96cf-bbf7859dc755"
        data = {
            "params": '{"client_input_params":{"username_input":'
            + self._username
            + ',"aac":"{\\"aac_init_timestamp\\":'
            + utils.get_pigeon_raw_client_time().split(".")[0]
            + ',\\"aacjid\\":\\"'
            + self._aacjid
            + '\\"}","lois_settings":{"lois_token":""},"zero_balance_state":"","network_bssid":null},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":"vanilla_ld","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"device_id":"'
            + self._android_id
            + '","offline_experiment_group":"caa_iteration_v3_perf_ig_4","waterfall_id":"'
            + self._waterfall_id
            + '","access_flow_version":"pre_mt_behavior","INTERNAL__latency_qpl_instance_id":2.04571724300113E14,"is_from_logged_in_switcher":0,"is_platform_login":0,"qe_device_id":"'
            + self._device_id
            + '"}}',
            "bk_client_context": '{"bloks_version":"'
            + self._blocks_version
            + '","styles_id":"instagram"}',
            "bloks_versioning_id": self._blocks_version,
        }

        response = await self._client.post(
            url="https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.login.oauth.token.fetch.async/",
            headers=heads,
            form=data,
        )

        return response

    async def create_keystore(self):
        heads = headers_import.get_create_keystore_headers(
            device_id=self._device_id,
            user_agent=self._user_agent,
            app_id=self._app_id,
            blocks_version=self._blocks_version,
            android_id=self._android_id,
            pigeon_raw_client_time=utils.get_pigeon_raw_client_time(),
            pigeon_session_id=self._pigeon_session_id,
        )
        data = {
            "app_scoped_device_id": self._device_id,
            "key_hash": "",
        }

        response = await self._client.post(
            url="https://b.i.instagram.com/api/v1/attestation/create_android_keystore/",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self._challenge_nonce = response_json["challenge_nonce"]
        self._key_nonce = response_json["key_nonce"]

        return response

    async def send_login_request(self) -> Response:
        sending_time = utils.get_pigeon_raw_client_time()
        encrypted_password = utils.encrypt_password(
            int(sending_time.split(".")[0]),
            int(self._encryption_key_id),
            self._encryption_pub_key,
            self._password,
        )
        heads = headers_import.get_send_login_headers(
            device_id=self._device_id,
            user_agent=self._user_agent,
            app_id=self._app_id,
            blocks_version=self._blocks_version,
            android_id=self._android_id,
            family_device_id=self._family_device_id,
            pigeon_raw_client_time=sending_time,
            pigeon_session_id=self._pigeon_session_id,
            x_mid=self._mid,
            challenge_nonce=self._challenge_nonce,
        )

        data = {
            "params": '{"client_input_params":{"aac":"{\\"aac_init_timestamp\\":'
            + str(int(sending_time.split(".")[0]) - 40)
            + ',\\"aacjid\\":\\"'
            + self._aacjid
            + '\\"}","sim_phones":[],"aymh_accounts":[],"network_bssid":null,"secure_family_device_id":"","has_granted_read_contacts_permissions":0,"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"'
            + encrypted_password
            + '","sso_token_map_json_string":"","block_store_machine_id":"","ig_vetted_device_nonces":null,"cloud_trust_token":null,"event_flow":"login_manual","password_contains_non_ascii":"false","client_known_key_hash":"","encrypted_msisdn":"","has_granted_read_phone_permissions":0,"app_manager_id":"","should_show_nested_nta_from_aymh":0,"device_id":"'
            + self._android_id
            + '","zero_balance_state":"","login_attempt_count":1,"machine_id":"'
            + self._mid
            + '","flash_call_permission_status":{"READ_PHONE_STATE":"DENIED","READ_CALL_LOG":"DENIED","ANSWER_PHONE_CALLS":"DENIED"},"accounts_list":[],"family_device_id":"'
            + self._family_device_id
            + '","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":""},"event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"contact_point":"'
            + self._username
            + '"},"server_params":{"should_trigger_override_login_2fa_action":0,"is_vanilla_password_page_empty_password":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'
            + self._waterfall_id
            + '","two_step_login_type":"one_step_login","login_source":"Login","is_platform_login":0,"INTERNAL__latency_qpl_marker_id":36707139,"is_from_aymh":0,"offline_experiment_group":"caa_iteration_v3_perf_ig_4","is_from_landing_page":0,"left_nav_button_action":"NONE","password_text_input_id":"'
            + self._input_ids.password_id
            + '","is_from_empty_password":0,"is_from_msplit_fallback":0,"ar_event_source":"login_home_page","qe_device_id":"'
            + self._device_id
            + '","username_text_input_id":"'
            + self._input_ids.username_id
            + '","layered_homepage_experiment_group":"vanilla_ld","device_id":"'
            + self._android_id
            + '","INTERNAL__latency_qpl_instance_id":2.04571724300364E14,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":null,"is_from_assistive_id":0,"access_flow_version":"pre_mt_behavior","is_from_logged_in_switcher":0}}',
            "bk_client_context": '{"bloks_version":"'
            + self._blocks_version
            + '","styles_id":"instagram"}',
            "bloks_versioning_id": self._blocks_version,
        }

        response = await self._client.post(
            url="https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.async.send_login_request/",
            headers=heads,
            form=data,
            verify=False,
        )

        response_json = await response.json()

        return response

    async def set_registration_credentials(
        self,
        email: str,
        name: str,
        username: str,
        password: str,
        birthdate: str,
        confirmation_code: str | None = None,
        safetynet_token: str | None = None,
    ):
        self._reg_credentials: RegData = RegData(
            email=email,
            name=name,
            username=username,
            password=password,
            birthdate=birthdate,
            confirmation_code=confirmation_code,
            safetynet_token=safetynet_token,
        )

    async def registration_button_click(self):
        heads = headers_import.register_click_headers(self)

        data = body_import.get_register_click_body(self.data)

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self._reg_info: RegInfo = utils.get_reg_info(response_json)

        self._reg_context = utils.get_reg_context(response_json)

        return response

    async def registration_phone_point(self):
        heads = headers_import.get_phone_request_headers(self.data)

        data = body_import.get_phone_request_body(self.data)

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        return response

    async def registration_email_point(self):
        heads = headers_import.get_email_submit_headers(self.data)

        data = body_import.get_email_click_body(self.data)

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id.append(
            utils.get_qpl_instance_id(
                str(
                    response_json["layout"]["bloks_payload"][
                        "embedded_payloads"
                    ]
                )
            )
        )

        return response

    async def send_email_request(self):
        heads = headers_import.get_email_submit_headers(self.data)

        data = {}

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id.append(
            utils.get_qpl_instance_id(
                str(
                    response_json["layout"]["bloks_payload"][
                        "embedded_payloads"
                    ]
                )
            )
        )

        return response

    async def confirmation_code_request(self):
        heads = headers_import.get_confirmation_request_headers(self.data)

        data = {}

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id.append(
            utils.get_qpl_instance_id(
                str(
                    response_json["layout"]["bloks_payload"][
                        "embedded_payloads"
                    ]
                )
            )
        )

        return response

    async def password_creation_request(self):
        heads = headers_import.get_password_create_headers(self.data)

        data = {}

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id.append(
            utils.get_qpl_instance_id(
                str(
                    response_json["layout"]["bloks_payload"][
                        "embedded_payloads"
                    ]
                )
            )
        )

        return response

    async def birthdate_request(self):
        heads = headers_import.get_birth_headers(self.data)

        data = {}

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id.append(
            utils.get_qpl_instance_id(
                str(
                    response_json["layout"]["bloks_payload"][
                        "embedded_payloads"
                    ]
                )
            )
        )

        return response

    async def name_request(self):
        heads = headers_import.get_name_headers(self.data)

        data = {}

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id.append(
            utils.get_qpl_instance_id(
                str(
                    response_json["layout"]["bloks_payload"][
                        "embedded_payloads"
                    ]
                )
            )
        )

        return response

    async def username_request(self):
        heads = headers_import.get_email_submit_headers(self.data)

        data = {}

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id = utils.get_qpl_instance_id(
            str(response_json["layout"]["bloks_payload"]["embedded_payloads"])
        )

        return response

    async def agreements_request(self):
        heads = headers_import.get_agreement_headers(self.data)

        data = body_import.get_agreement_body(self.data)

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self.data.qpl_instance_id = utils.get_qpl_instance_id(
            str(response_json["layout"]["bloks_payload"]["embedded_payloads"])
        )

        return response

    async def set_registration_data(
        self,
        email: str,
        name: str,
        username: str,
        password: str,
        birthdate: str,
    ):
        self.data = RegistrationData(
            android_id=self._android_id,
            family_device_id=self._family_device_id,
            waterfall_id=self._waterfall_id,
            device_id=self._device_id,
            app_id=self._app_id,
            bloks_version=self._blocks_version,
            user_agent=self._user_agent,
            aacjid=self._aacjid,
            qpl_instance_id=self.qpl_instance_id,
            qpl_marker_id=self.qpl_marker_id,
            name=name,
            username=self.username,
            email=email,
            encrypted_password=utils.encrypt_password(
                float(utils.get_pigeon_raw_client_time() * 1000),
                self._encryption_key_id,
                self._encryption_pub_key,
                password,
            ),
            raw_password=password,
            zero_eh="IG0e09d776530888418ab70f3822fbb4e1",
        )

    async def registration_flow(self):
        self.set_registration_data(
            email="example@example.com",
            name="Example Name",
            username="exampleuser",
            password="examplepass",
            birthdate="2000-01-01",
        )

    async def login_flow(self) -> Response:
        print("[*] Starting mobile config...")
        config = await self.mobile_config()
        print(config.status)
        print("[*] Mobile config done.")
        dual = await self.dual_token()
        print(dual.status)
        print("[*] Dual token fetched.")
        print("[*] Processing and redirecting...")
        proc = await self.process_and_redirect()
        print("[*] Process and redirect done.")
        some = await self.token_fetch()
        print(some.status)
        print("[*] Token fetch done.")
        keystore = await self.create_keystore()
        print(keystore.status)
        print("[*] Keystore created.")
        await asyncio.sleep(2)
        proc = await self.send_login_request()
        print(proc.status)
        print("[*] Login request sent.")

        return proc

    def __repr__(self):
        return f"<Flow username={self._username} device_id={self._device_id} pigeon_session_id={self._pigeon_session_id} mid={self._mid}> autorization = {self._token}"


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

    some: RegData = RegData(
        email="bomarqstutiapt@outlook.com",
        password="uaY24zRCsjAj7x@Instagram",
        name="Eugene",
        username="omarqstutiapt",
        birth_date="15-08-2002",
    )
    some: RegistrationFlow = RegistrationFlow(some)

    response = await some.run()
    response_json = await response.json()

    print(response_json)
    print(response_json)


if __name__ == "__main__":
    asyncio.run(main())
