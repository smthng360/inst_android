import src.flow.utils as utils
from src.flow.consts import INSTAGRAM_VERSION, APP_ID, BLOKS_VERSION_ID
from rnet import Client, Emulation, Proxy
import src.flow.headers as headers_import
import json


class PhoneSetup:
    def __init__(self, username: str):
        self._username: str = username

        self._device_id: str = utils.generate_ig_device_id(self._username)
        self._family_device_id: str = utils.generate_family_device_id(
            self._username
        )
        self._android_id: str = utils.generate_android_id(self._username)
        self._pigeon_session_id: str = utils.create_pigeon_session_id()
        self._mid: str = utils.generate_mid()
        self._log_seq: int = 0

        self._token: str = None

        self._picked_instagram_version: str = INSTAGRAM_VERSION
        self._waterfall_id: str = utils.generate_waterfall_id()
        self._app_id: str = APP_ID
        self._blocks_version: str = BLOKS_VERSION_ID
        self._user_agent: str = utils.get_user_agent()

        self._conn_uuid_client: str = None

        self._aacjid: str = None
        self._aac_init_timestamp: int = None

        self._key_nonce: str = None
        self._challenge_nonce: str = None

        self._client = Client(
            emulation=Emulation.OkHttp3_14,
            proxy=Proxy.all("http://127.0.0.1:8000"),
            verify=False,
        )

        self._experiment_group: str = "caa_iteration_v3_perf_ig_4"

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
            url="https://b.i.instagram.com/api/v1/zr/dual_tokens/",
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

        for k, v in data.items():
            print(
                f"  {k:20} → type={type(v).__name__}, len={len(v) if isinstance(v, (str, bytes)) else 'n/a'}"
            )

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
            print("AACJID found in response, extracting...")
            print(response_json["layout"]["bloks_payload"]["data"][-1]["data"]["initial_lispy"])
            self._aacjid = utils.get_aacjid(
                response_json["layout"]["bloks_payload"]["data"][-1]["data"][
                    "initial_lispy"
                ]
            )
            self._aac_init_timestamp = utils.get_aac_init_timestamp(
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
        ).decode("utf-8")
        self._encryption_key_id = int(response.headers.get(
            "Ig-Set-Password-Encryption-Key-Id", None
        ).decode("utf-8"))

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
        print(response.headers.get("Ig-Set-X-Mid"))
        mid = response.headers.get("Ig-Set-X-Mid")
        self._mid = str(mid)

        return response
