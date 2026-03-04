from datetime import datetime, timezone, timedelta
from os import name
from rnet import OrigHeaderMap, Response, Proxy, HeaderMap
from src.schema import RegData, EmailResponse
from .schemas import BloksPayloadType, RegistrationDict
import src.flow.headers as headers_import
import src.flow.utils as utils
from src.flow.basic import PhoneSetup
import json
from src.flow.mail import fetch_latest_message
import asyncio


class RegistrationFlow(PhoneSetup):
    def __init__(self, data: RegData):
        if not data.username:
            data.username = data.email.split("@")[0]
        super().__init__(data.username)
        self._email: str = data.email
        self._raw_password: str = data.password
        self._email_client_id: str = data.email_client_id
        self._refresh_token: str = data.refresh_token
        self._name: str = data.name
        self._confirmation_code: str = data.confirmation_code
        self._birth_date: str = data.birth_date
        self._safetynet_token: str | None = data.safetynet_token

        self._registration_context_token: str = None
        self._registration_dictionary: RegistrationDict | None = None

        self._encryption_key_id: int | None = None
        self._encryption_pub_key: str | None = None

        self._qpl_marker_id: int | None = None
        self._qpl_instance_id: float | None = None

        self._zero_eh: str | None = (
            "IG0e09d776530888418ab70f3822fbb4e1"  # inspect this on real device
        )
        self._conn_uuid_client: str | None
        self._aacjid: str | None = None

        self._event_id: list[str] = []
        self._current_inputs: list[int] = []


    async def make_graphql_request(
        self,
        heads: HeaderMap,
        data,
        new_url: str | None = "https://b.i.instagram.com/graphql_www",
        orig_heads: OrigHeaderMap = None,
    ) -> Response:
        prox = Proxy.all("http://127.0.0.1:8080")

        response = await self._client.post(
            url=new_url,
            headers=heads,
            form=data,
            orig_headers=orig_heads,
            proxy=prox,
        )
        return response

    async def process_and_redirect(self) -> Response:
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
            self._aac_init_timestamp = utils.get_aac_init_timestamp(
                response_json["layout"]["bloks_payload"]["data"][-1]["data"][
                    "initial_lispy"
                ]
            )

        ids = utils.get_input_ids(str(response_json["layout"]))

        self._input_ids = ids

        some = utils.get_qpl_ids(
            str(response_json["layout"]["bloks_payload"]["embedded_payloads"])
        )

        self._qpl_marker_id, self._qpl_instance_id = (
            some if some else (36707139, 1.30274154100123)
        )

        return response

    async def register_button_click(self) -> Response:
        heads = headers_import.get_register_click_headers(self)

        variables = {
            "client_input_params": {
                "should_show_nested_nta_bottom_sheet": 0,
                "accounts_list": [],
                "username_input": "",
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "device_emails": [],
                "lois_settings": {"lois_token": ""},
                "zero_balance_state": "",
                "network_bssid": None,
                "device_phone_numbers": [],
            },
            "server_params": {
                "is_from_logged_out": 0,
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "should_expand_layered_bottom_sheet": 0,
                "is_from_lid_welcome_screen": 0,
                "device_id": self._android_id,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,
                "reg_flow_source": "login_home_native_integration_point",
                "is_caa_perf_enabled": 1,
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,
                "family_device_id": None,
                "offline_experiment_group": self._experiment_group,
                "entrypoint": "login_home_async",
                "access_flow_version": "pre_mt_behavior",
                "is_eligible_for_igds_sac_reg_flow": 0,
                "is_from_logged_in_switcher": 0,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",  # static for this request
            "client_doc_id": "356548512614739681018024088968",  # inspect what is client doc id
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }
        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open(
            "register_button_click_response.json", "w", encoding="utf-8"
        ) as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        self._registration_dictionary = utils.get_registration_dictionary(
            response_json,
        )

        self._registration_context_token = utils.get_registration_context_token(
            response_json
        )

        return response

    async def contact_point_phone(self) -> Response:
        heads = headers_import.get_phone_request_headers(self)

        variables = {
            "client_input_params": {
                "family_device_id": self._family_device_id,
                "block_store_machine_id": "",
                "device_id": self._android_id,
                "lois_settings": {"lois_token": ""},
                "waterfall_id": self._waterfall_id,
                "cloud_trust_token": "None",
                "machine_id": self._mid,
                "qe_device_id": self._device_id,
            },
            "server_params": {
                "is_from_logged_out": 0,
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "device_id": self._android_id,
                "reg_context": self._registration_context_token,
                "waterfall_id": self._waterfall_id,
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "reg_info": self._registration_dictionary,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "INTERNAL_INFRA_screen_id": "CAA_REG_CONTACT_POINT_PHONE",
                "access_flow_version": "pre_mt_behavior",
                "qe_device_id": self._device_id,
                "current_step": 0,
            },
        }

        innermost = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle = json.dumps(
            {"params": innermost}, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.contactpoint_phone",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.contactpoint_phone",
            "client_doc_id": "253360298312778871684788706414",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": json.dumps(variables),
        }

        response = await self._client.post(
            url="https://b.i.instagram.com/graphql_www",
            headers=heads,
            form=data,
        )

        response_json = await response.json()

        self._registration_dictionary = utils.get_registration_dictionary(
            response_json, bloks_type=BloksPayloadType.APP
        )
        self._registration_context_token = utils.get_registration_context_token(
            response_json, bloks_type=BloksPayloadType.APP
        )

        self._event_id.append(utils.extract_event_id(str(response_json)))

        return response

    async def contact_point_email(self) -> Response:
        heads = headers_import.get_email_button_headers(self)

        variables = {
            "client_input_params": {
                "lois_settings": {"lois_token": ""},
                "zero_balance_state": "",
            },
            "server_params": {
                "is_from_logged_out": 0,
                "root_screen_id": "bloks.caa.reg.contactpoint_phone",
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "device_id": self._android_id,
                "waterfall_id": self._waterfall_id,
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "family_device_id": self._family_device_id,
                "reg_info": self._registration_dictionary,
                "offline_experiment_group": self._experiment_group,
                "INTERNAL_INFRA_screen_id": "CAA_REG_CONTACT_POINT_EMAIL",
                "access_flow_version": "pre_mt_behavior",
                "qe_device_id": self._device_id,
                "current_step": 0,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.contactpoint_email",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }

        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.contactpoint_email",
            "client_doc_id": "253360298312778871684788706414",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open(
            "contact_point_email_response.json", "w", encoding="utf-8"
        ) as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        self._registration_dictionary = utils.get_registration_dictionary(
            response_json, bloks_type=BloksPayloadType.APP
        )
        self._registration_context_token = utils.get_registration_context_token(
            response_json, bloks_type=BloksPayloadType.APP
        )

        self._email_input_id = utils.find_email_input_id(
            json.dumps(response_json)
        )

        self._event_id.append(utils.extract_event_id(str(response_json)))

        return response

    async def email_submit_button(self) -> Response:
        heads = headers_import.get_email_submit_headers(self)

        variables = {
            "client_input_params": {
                "aac": json.dumps(
                    {
                        "aac_init_timestamp": self._aac_init_timestamp,
                        "aacjid": self._aacjid,
                    }
                ),
                "lois_settings": {"lois_token": ""},
                "zero_balance_state": "",
                "device_id": self._android_id,
                "network_bssid": None,
                "msg_previous_cp": "",
                "email_token": "",
                "switch_cp_first_time_loading": 1,
                "accounts_list": [],
                "email_prefilled": 0,
                "confirmed_cp_and_code": {},
                "family_device_id": self._family_device_id,
                "block_store_machine_id": "",
                "fb_ig_device_id": [],
                "cloud_trust_token": None,
                "is_from_device_emails": 0,
                "email": self._email,
                "switch_cp_have_seen_suma": 0,
            },
            "server_params": {
                "event_request_id": self._event_id[-1],
                "is_from_logged_out": 0,
                "text_input_id": int(self._email_input_id),
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,
                "flow_info": json.dumps(
                    {
                        "flow_name": "new_to_family_ig_default",
                        "flow_type": "ntf",
                    }
                ),
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": self._experiment_group,
                "cp_funnel": 0,
                "cp_source": 0,
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0,
                "current_step": 0,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.async.contactpoint_email.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }

        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open("email_submit_response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        with open("email_submit_full.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )

        with open("email_submit_full.txt", "w", encoding="utf-8") as f:
            f.write(str(response_json))

        event_id, self._confirmation_code_input_id = (
            utils.get_confirmation_code_input_id(str(response_json))
        )

        self._event_id.append(event_id)

        self._registration_dictionary = utils.get_registration_dictionary(
            response_json
        )
        self._registration_context_token = utils.get_registration_context_token(
            response_json
        )

        self._qpl_instance_id = utils.get_qpl_for_confirmation_code(
            str(response_json)
        )

        return response

    async def confirm_email_with_code(self) -> Response:
        await self.set_confirmation_code()

        if "has_seen_confirmation_screen" in self._registration_dictionary:
            self._registration_dictionary = json.loads(
                self._registration_dictionary
            )

            self._registration_dictionary["has_seen_confirmation_screen"] = (
                False
            )

            self._registration_dictionary[
                "fb_email_login_upsell_skip_suma_post_tos"
            ] = False

            self._registration_dictionary = json.dumps(
                self._registration_dictionary,
                separators=(",", ":"),
                ensure_ascii=False,
            )

        if self._confirmation_code is None:
            raise ValueError("Confirmation code is not set.")

        heads = headers_import.get_confirmation_request_headers(self)

        variables = {
            "client_input_params": {
                "confirmed_cp_and_code": {},
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "block_store_machine_id": "",
                "code": f"{self._confirmation_code}",
                "fb_ig_device_id": [],
                "device_id": self._android_id,
                "lois_settings": {"lois_token": ""},
                "cloud_trust_token": None,
                "network_bssid": None,
            },
            "server_params": {
                "event_request_id": self._event_id[
                    -1
                ],  # get from "next button click request"
                "is_from_logged_out": 0,
                "text_input_id": int(
                    self._confirmation_code_input_id
                ),  # get from "next button click request"
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                ## below is "pre_mt_behavior"
                "reg_context": self._registration_context_token,
                "waterfall_id": self._waterfall_id,
                "wa_timer_id": "wa_retriever",
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,  # get from "next button click request"
                "flow_info": json.dumps(
                    {
                        "flow_name": "new_to_family_ig_default",
                        "flow_type": "ntf",
                    },
                    separators=(",", ":"),
                    ensure_ascii=False,
                ),
                "is_platform_login": 0,
                "sms_retriever_started_prior_step": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,  # get from "next button click request"
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0,
                "current_step": 3,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.confirmation.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        variables = variables.replace(
            r"\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040"
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        heads_map = OrigHeaderMap(([x for x in heads.keys()]))
        response = await self.make_graphql_request(
            new_url="https://b.i.instagram.com/graphql_www",
            heads=heads,
            orig_heads=heads_map,
            data=data,
        )
        try:
            body = await response.text()
        except Exception:
            raw = await response.bytes()
            body = bytes(raw).decode("utf-8", errors="replace")

        with open("confirm_email_response.json", "w", encoding="utf-8") as f:
            json.dump(json.loads(body), f, ensure_ascii=False, indent=4)

        with open("confirm_email_full.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )

        self._registration_dictionary = utils.get_registration_dictionary(
            json.loads(body)
        )
        self._registration_context_token = utils.get_registration_context_token(
            json.loads(body)
        )

        self._event_id.append(utils.extract_event_id(body))

        return response

    async def set_confirmation_code(
        self,
    ) -> Response:
        if self._confirmation_code:
            return

        submission_time = datetime.now(timezone.utc).replace(
            microsecond=0, second=0
        )  # round down to nearest minute
        timeout_seconds = 120
        poll_interval = 5
        deadline = submission_time + timedelta(seconds=timeout_seconds)

        while datetime.now(timezone.utc) < deadline:
            message = await fetch_latest_message(
                email=self._email,
                client_id=self._email_client_id,
                refresh_token=self._refresh_token,
                submission_time=submission_time,
            )

            if isinstance(message, EmailResponse) and message.code:
                self._confirmation_code = message.code
                return

            await asyncio.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for confirmation email.")

    async def password_creation(self) -> Response:
        heads = headers_import.get_password_create_headers(self)

        encrypted_password = utils.encrypt_password(
            raw_client_time=utils.get_pigeon_raw_client_time(),
            raw_password=self._raw_password,
            key_id=self._encryption_key_id,
            pub_key=self._encryption_pub_key,
        )

        variables = {
            "client_input_params": {
                "spi_action": 1,
                "safetynet_response": "API_ERROR: class com.google.android.gms.common.api.ApiException:7: ",  #### important note here
                "caa_play_integrity_attestation_result": "",
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "safetynet_token": utils.safetynet_token(
                    self._email,
                    int(utils.get_pigeon_raw_client_time().split(".")[0]),
                ),
                "whatsapp_installed_on_client": 0,
                "zero_balance_state": "",
                "network_bssid": "None",
                "machine_id": self._mid,
                "headers_last_infra_flow_id_safetynet": "",
                "system_permissions_status": {
                    "READ_CONTACTS": "DENIED",
                    "GET_ACCOUNTS": "DENIED",
                    "READ_PHONE_STATE": "DENIED",
                    "READ_PHONE_NUMBERS": "DENIED",
                },
                "email_oauth_token_map": {},
                "block_store_machine_id": "",
                "fb_ig_device_id": [],
                "encrypted_msisdn_for_safetynet": "",
                "lois_settings": {"lois_token": ""},
                "cloud_trust_token": None,
                "client_known_key_hash": "",
                "encrypted_password": encrypted_password,
            },
            "server_params": {
                "event_request_id": self._event_id[
                    -1
                ],  # from confirmation code request
                "flow_modifier": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_from_logged_out": 0,
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                # from confirmation code request
                "reg_context": self._registration_context_token,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,  # from previous code request
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,  # from confirmation code request
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": self._experiment_group,
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0,
                "current_step": 4,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.password.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        variables = variables.replace(
            r"\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040"
        )

        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.password.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open("password_creation_request.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )

        with open(
            "password_creation_response.json", "w", encoding="utf-8"
        ) as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        self._registration_context_token = utils.get_registration_context_token(
            response_json
        )
        self._registration_dictionary = utils.get_registration_dictionary(
            response_json
        )
        self._qpl_marker_id, self._qpl_instance_id = (
            utils.get_qpl_after_password(str(response_json))
        )

        self._event_id.append(utils.extract_event_id(str(response_json)))

        return response

    async def birthday_adding(self) -> Response:
        heads = headers_import.get_birth_headers(self)

        variables = {
            "client_input_params": {
                "client_timezone": "Europe/Kiev",
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "birthday_or_current_date_string": self._birth_date,
                "os_age_range": "",
                "birthday_timestamp": utils.date_to_unix_timestamp(
                    self._birth_date
                ),
                "lois_settings": {"lois_token": ""},
                "zero_balance_state": "",
                "network_bssid": None,
                "should_skip_youth_tos": 0,
                "is_youth_regulation_flow_complete": 0,
            },
            "server_params": {
                "is_from_logged_out": 0,
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                # from password_creation_request
                "reg_context": self._registration_context_token,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,  # from password_creation_request
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,  # from password_creation_request
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": self._experiment_group,
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0,
                "current_step": 6,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.birthday.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        variables = variables.replace(
            r"\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040"
        )

        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.birthday.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open("birthday_adding_response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        with open("birthday_adding_request.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )

        self._registration_context_token = utils.get_registration_context_token(
            response_json
        )
        self._registration_dictionary = utils.get_registration_dictionary(
            response_json
        )

        self._qpl_marker_id, self._qpl_instance_id = (
            utils.get_qpl_after_birthdate(str(response_json))
        )

        self._event_id.append(utils.extract_event_id(str(response_json)))

        return response

    async def name_adding(self) -> Response:
        heads = headers_import.get_name_headers(self)

        variables = {
            "client_input_params": {
                "accounts_list": [],
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "lois_settings": {"lois_token": ""},
                "zero_balance_state": "",
                "network_bssid": None,
                "name": self._name,
            },
            "server_params": {
                "is_from_logged_out": 0,
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                # check from birthday request
                "reg_context": self._registration_context_token,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,  # check from birthday request
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,  # check from birthday request
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "access_flow_version": "pre_mt_behavior",
                "is_from_logged_in_switcher": 0,
                "current_step": 7,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.name_ig_and_soap.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        variables = variables.replace(
            r"\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040"
        )

        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.name_ig_and_soap.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open("name_adding_response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        with open("name_adding_request.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )

        self._registration_context_token = utils.get_registration_context_token(
            response_json
        )
        self._second_context_token = utils.get_registration_context_token(response_json, position=-2)
        self._registration_dictionary = utils.get_registration_dictionary(
            response_json
        )

        self._qpl_marker_id, self._qpl_instance_id = utils.get_qpl_after_name(
            str(response_json)
        )

        self._event_id.append(utils.extract_event_id(str(response_json)))

        self._current_inputs = utils.find_reg_inputs(str(response_json))[4:]

        return response
    
    async def username_first(self) -> Response:
        heads = headers_import.get_username_headers(self)


        variables = {
            "client_input_params": {
                "validation_text": self._username,
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":'
                + self._aacjid
                + "}",
                "family_device_id": self._family_device_id,
                "device_id": self._android_id,
                "lois_settings": {"lois_token": ""},
                "network_bssid": "None",
                "qe_device_id": self._device_id,
            },
            "server_params": {
                "is_from_logged_out": 0,
                "text_input_id": int(self._current_inputs[3]),
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "serialized_states": {"current_text": "4;1asfxakb73;0"},
                "device_id": self._device_id,
                "reg_context": self._registration_context_token,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": self._experiment_group,
                "suggestions_container_id": self._current_inputs[2],
                "action": 0,
                "screen_id": self._current_inputs[0],
                "access_flow_version": "pre_mt_behavior",
                "post_tos": 0,
                "input_id": self._current_inputs[1],
                "is_from_logged_in_switcher": 0,
                "current_step": 8,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.username.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        variables = variables.replace(
            r"\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040"
        )

        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.username.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open("username_adding_response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        with open("username_adding_request.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )
        

        return response
    
    async def username_submit(self) -> Response:
        heads = headers_import.get_username_headers(self)

        self._registration_dictionary = json.loads(self._registration_dictionary)
        del self._registration_dictionary['has_seen_confirmation_screen']
        del self._registration_dictionary['flash_call_nonce_prefix_details']
        del self._registration_dictionary['is_in_gms_experience']
        del self._registration_dictionary['is_in_nta_single_form']
        del self._registration_dictionary['fb_email_login_upsell_skip_suma_post_tos']

        self._registration_dictionary = json.dumps(self._registration_dictionary, separators=(",", ":"), ensure_ascii=False)
        
        variables = {
            "client_input_params": {
                "validation_text": self._username,
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":'
                + self._aacjid
                + '"}'  ,
                "family_device_id": self._family_device_id,
                "device_id": self._android_id,
                "lois_settings": {"lois_token": ""},
                "network_bssid": "null",
                "qe_device_id": self._device_id,
            },
            "server_params": {
                "event_request_id": self._event_id[-1],
                "is_from_logged_out": 0,
                "text_input_id": int(self._current_inputs[3]),
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                "reg_context": self._second_context_token,
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": self._experiment_group,
                "suggestions_container_id": int(self._current_inputs[2]),
                "action": 1,
                "screen_id": int(self._current_inputs[0]),
                "access_flow_version": "pre_mt_behavior",
                "post_tos": 0,
                "input_id": int(self._current_inputs[0])-8,
                "is_from_logged_in_switcher": 0,
                "current_step": 8,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.username.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )


        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.username.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        response = await self.make_graphql_request(heads, data)

        response_json = await response.json()

        with open("username_adding_response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        with open("username_adding_request.json", "w", encoding="utf-8") as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )
        

        self._registration_context_token = utils.get_registration_context_token(
            response_json
        )

        self._registration_dictionary = utils.get_registration_dictionary(
            response_json
        )

        self._qpl_marker_id, self._qpl_instance_id = utils.get_qpl_after_username_submit(
            str(response_json)
        )


        return response



    async def agreement_acceptance(self) -> Response:
        heads = headers_import.get_agreement_headers(self)

        self._registration_dictionary = json.loads(self._registration_dictionary)

        del self._registration_dictionary["sk_pipa_consent_given"]
        self._registration_dictionary["is_wanted_suma_user"] = None
        self._registration_dictionary['has_seen_confirmation_screen'] = False
        self._registration_dictionary["ignore_suma_check"] = False
        self._registration_dictionary["did_use_age"] = False

        self._registration_dictionary = json.dumps(self._registration_dictionary, separators=(",", ":"), ensure_ascii=False)

        variables = {
            "client_input_params": {
                "ck_error": "",
                "aac": '{"aac_init_timestamp":'
                + str(self._aac_init_timestamp)
                + ',"aacjid":"'
                + self._aacjid
                + '"}',
                "device_id": self._android_id,
                "waterfall_id": self._waterfall_id,
                "zero_balance_state": "",
                "network_bssid": None,
                "failed_birthday_year_count": "",
                "headers_last_infra_flow_id": "",
                "ig_partially_created_account_nonce_expiry": 0,
                "machine_id": "aXFTbgABAAHw1cpzzsgkxOLUNm6H",
                "should_ignore_existing_login": 0,
                "reached_from_tos_screen": 1,
                "ig_partially_created_account_nonce": "",
                "ck_nonce": "",
                "force_sessionless_nux_experience": 0,
                "lois_settings": {"lois_token": ""},
                "ig_partially_created_account_user_id": 0,
                "cloud_trust_token": None,
                "ck_id": "",
                "no_contact_perm_email_oauth_token": "",
                "encrypted_msisdn": "",
            },
            "server_params": {
                "event_request_id": self._event_id[-1],
                "is_from_logged_out": 0,
                "layered_homepage_experiment_group": "ld_no_language_selector",
                "device_id": self._android_id,
                "reg_context": self._registration_context_token,
                "login_surface": "unknown",
                "waterfall_id": self._waterfall_id,
                "INTERNAL__latency_qpl_instance_id": self._qpl_instance_id,
                "flow_info": '{"flow_name":"new_to_family_ig_default","flow_type":"ntf"}',
                "is_platform_login": 0,
                "should_ignore_suma_check": 0,
                "INTERNAL__latency_qpl_marker_id": self._qpl_marker_id,
                "bloks_controller_source": "bk_caa_reg_tos_screen",
                "reg_info": self._registration_dictionary,
                "family_device_id": self._family_device_id,
                "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                "access_flow_version": "pre_mt_behavior",
                "app_id": 0,
                "is_from_logged_in_switcher": 0,
                "current_step": 9,
                "qe_device_id": self._device_id,
            },
        }

        innermost_str = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        middle_dict = {"params": innermost_str}
        middle_str = json.dumps(
            middle_dict, separators=(",", ":"), ensure_ascii=False
        )

        variables = {
            "params": {
                "params": middle_str,
                "bloks_versioning_id": self._blocks_version,
                "infra_params": {
                    "device_id": self._device_id,
                },
                "app_id": "com.bloks.www.bloks.caa.reg.create.account.async",
            },
            "bk_context": {
                "is_flipper_enabled": False,
                "theme_params": [],
                "debug_tooling_metadata_token": None,
            },
        }
        variables = json.dumps(
            variables, separators=(",", ":"), ensure_ascii=False
        )

        variables = variables.replace(
            r"\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040"
        )

        variables = variables.replace(r"\\\\\\\\\\\\\\\\\\\\\\\\u0040", r"\\\\\\\\u0040")
        import re

        variables = re.sub(r'\\{15,}/', r'\\\\\\\\/', variables)

        variables = utils.remake_qpl_instace_id(
            variables, self._qpl_instance_id
        )

        data = {
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "user",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.create.account.async",
            "client_doc_id": "356548512614739681018024088968",
            "enable_canonical_naming": "true",
            "enable_canonical_variable_overrides": "true",
            "enable_canonical_naming_ambiguous_type_prefixing": "true",
            "variables": variables,
        }

        heads_map = OrigHeaderMap([
        "Host",
        "Accept-Language",
        'Content-Length',
        "Content-Type",
        "Priority",
        "User-Agent",
        "X-Bloks-Version-Id",
        "X-Client-Doc-Id",
        "X-Fb-Client-Ip",
        "X-Fb-Friendly-Name",
        "X-Fb-Request-Analytics-Tags",
        "X-Fb-Server-Cluster",
        "X-Ig-Android-Id",
        "X-Ig-App-Id",
        "X-Ig-Attest-Params",
        "X-Ig-Capabilities",
        "X-Ig-Device-Id",
        "X-Ig-Is-Foldable",
        "X-Ig-Timezone-Offset",
        "X-Ig-Validate-Null-In-Legacy-Dict",
        "X-Root-Field-Name",
        "X-Tigon-Is-Retry",
        'Accept-Encoding',
        "X-Fb-Conn-Uuid-Client",
        "X-Fb-Http-Engine",
        "X-Graphql-Client-Library",
        "X-Graphql-Request-Purpose",])


        response = await self.make_graphql_request(heads=heads, data=data, orig_heads=heads_map)

        response_json = await response.json()

        with open(
            "agreement_acceptance_response.json", "w", encoding="utf-8"
        ) as f:
            json.dump(response_json, f, ensure_ascii=False, indent=4)

        with open(
            "agreement_acceptance_request.json", "w", encoding="utf-8"
        ) as f:
            json.dump(
                {"heads": heads, "data": data}, f, ensure_ascii=False, indent=4
            )

        return response


    async def _step(self, name, coro):
        try:
            resp = await coro
            await asyncio.sleep(4)  # small delay to avoid hitting rate limits
            print(f"{name} -> OK:", getattr(resp, "status", resp))
            return resp
        except Exception as e:
            print(f"{name} -> ERROR:", e)
            with open("error_response.txt", "w", encoding="utf-8") as f:
                f.write(str(e))

            raise

    async def run(self):
        print("Starting registration flow...")

        dual_token_resp = await self._step(
            "Preparing device info (dual_token)", self.dual_token()
        )

        mobile_config_resp = await self._step(
            "Mobile config", self.mobile_config()
        )

        process_resp = await self._step(
            "Process and redirect", self.process_and_redirect()
        )

        andr_keystore = await self._step(
            "Android keystore", self.create_keystore()
        )

        print("Filling registration form...")

        register_resp = await self._step(
            "Register button click", self.register_button_click()
        )

        phone_resp = await self._step(
            "Contact point phone", self.contact_point_phone()
        )

        email_resp = await self._step(
            "Contact point email", self.contact_point_email()
        )

        email_submit_resp = await self._step(
            "Submitting email", self.email_submit_button()
        )

        confirm_resp = await self._step(
            "Confirming email with code", self.confirm_email_with_code()
        )

        password_resp = await self._step(
            "Adding password", self.password_creation()
        )

        birthday_resp = await self._step(
            "Adding birthday", self.birthday_adding()
        )

        name_resp = await self._step("Adding name", self.name_adding())

        username_resp = await self._step(
            "Choosing username", self.username_first()
        )

        username_resp = await self._step(
            "Choosing username", self.username_submit()
        )

        andr_keystore = await self._step(
            "Android keystore", self.create_keystore()
        )

        andr_keystore = await self._step(
            "Android keystore", self.create_android_playintegrity()
        )

        agreement_resp = await self._step(
            "Accepting agreement", self.agreement_acceptance()
        )

        print(agreement_resp)
