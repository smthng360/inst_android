import json

import requests
from src.utils import write_response
import os
import src.flow.utils as utils

headers = {
    "Host": "b.i.instagram.com",
    "Accept-Language": "en-US",
    # 'Content-Length': '3139',
    "Content-Type": "application/x-www-form-urlencoded",
    "Priority": "u=3, i",
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Bloks-Version-Id": "b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9",
    "X-Client-Doc-Id": "356548512614739681018024088968",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",
    "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"567067343352427","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
    "X-Fb-Server-Cluster": "True",
    "X-Ig-Android-Id": "android-f35f126bc4795e76",
    "X-Ig-App-Id": "567067343352427",
    "X-Ig-Capabilities": "3brTv10=",
    "X-Ig-Device-Id": "c734a1c7-d663-4fad-af07-817b064e424b",
    "X-Ig-Is-Foldable": "true",
    "X-Ig-Timezone-Offset": "7200",
    "X-Ig-Validate-Null-In-Legacy-Dict": "true",
    "X-Root-Field-Name": "bloks_action",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "X-Fb-Conn-Uuid-Client": "95b2bb513e6c590b7147b9e4bcf849d8",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    "X-Graphql-Client-Library": "pando",
    "X-Graphql-Request-Purpose": "fetch",
}

data = {
    "method": "post",
    "pretty": "false",
    "format": "json",
    "server_timestamps": "true",
    "locale": "user",
    "purpose": "fetch",
    "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",
    "client_doc_id": "356548512614739681018024088968",
    "enable_canonical_naming": "true",
    "enable_canonical_variable_overrides": "true",
    "enable_canonical_naming_ambiguous_type_prefixing": "true",
    "variables": '{"params":{"params":"{\\"params\\":\\"{\\\\\\"client_input_params\\\\\\":{\\\\\\"should_show_nested_nta_bottom_sheet\\\\\\":0,\\\\\\"accounts_list\\\\\\":[],\\\\\\"username_input\\\\\\":\\\\\\"\\\\\\",\\\\\\"aac\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"aac_init_timestamp\\\\\\\\\\\\\\":1769034606,\\\\\\\\\\\\\\"aacjid\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"d2c8ed10-f952-4a12-aa09-e83671b1bf71\\\\\\\\\\\\\\"}\\\\\\",\\\\\\"device_emails\\\\\\":[],\\\\\\"lois_settings\\\\\\":{\\\\\\"lois_token\\\\\\":\\\\\\"\\\\\\"},\\\\\\"zero_balance_state\\\\\\":\\\\\\"\\\\\\",\\\\\\"network_bssid\\\\\\":null,\\\\\\"device_phone_numbers\\\\\\":[]},\\\\\\"server_params\\\\\\":{\\\\\\"is_from_logged_out\\\\\\":0,\\\\\\"layered_homepage_experiment_group\\\\\\":\\\\\\"ld_no_language_selector\\\\\\",\\\\\\"should_expand_layered_bottom_sheet\\\\\\":0,\\\\\\"is_from_lid_welcome_screen\\\\\\":0,\\\\\\"device_id\\\\\\":\\\\\\"android-f35f126bc4795e76\\\\\\",\\\\\\"waterfall_id\\\\\\":\\\\\\"d6031628-57e9-4414-93ad-9911cf738e0b\\\\\\",\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\":1.30180011200266E14,\\\\\\"reg_flow_source\\\\\\":\\\\\\"login_home_native_integration_point\\\\\\",\\\\\\"is_caa_perf_enabled\\\\\\":1,\\\\\\"is_platform_login\\\\\\":0,\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\":36707139,\\\\\\"family_device_id\\\\\\":null,\\\\\\"offline_experiment_group\\\\\\":\\\\\\"caa_iteration_v3_perf_ig_4\\\\\\",\\\\\\"entrypoint\\\\\\":\\\\\\"login_home_async\\\\\\",\\\\\\"access_flow_version\\\\\\":\\\\\\"pre_mt_behavior\\\\\\",\\\\\\"is_eligible_for_igds_sac_reg_flow\\\\\\":0,\\\\\\"is_from_logged_in_switcher\\\\\\":0,\\\\\\"qe_device_id\\\\\\":\\\\\\"c734a1c7-d663-4fad-af07-817b064e424b\\\\\\"}}\\"}","bloks_versioning_id":"b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9","infra_params":{"device_id":"c734a1c7-d663-4fad-af07-817b064e424b"},"app_id":"com.bloks.www.bloks.caa.reg.aymh_create_account_button.async"},"bk_context":{"is_flipper_enabled":false,"theme_params":[],"debug_tooling_metadata_token":null}}',
}

response = requests.post(
    "https://b.i.instagram.com/graphql_www",
    headers=headers,
    data=data,
    verify=False,
)

write_response(response, os.path.dirname(__file__))

from src.schema import RegistrationData


def register_click_body(
    data: RegistrationData,
) -> dict:
    variables = {
        "client_input_params": {
            "should_show_nested_nta_bottom_sheet": 0,
            "accounts_list": [],
            "username_input": "",
            "aac": '{"aac_init_timestamp":'
            + utils.get_pigeon_raw_client_time().split(".")[0]
            + ',"aacjid":"'
            + data.aacjid
            + '"}',
            "device_emails": [],
            "lois_settings": {"lois_token": ""},
            "zero_balance_state": "",
            "network_bssid": "None",
            "device_phone_numbers": [],
        },
        "server_params": {
            "is_from_logged_out": 0,
            "layered_homepage_experiment_group": "ld_no_language_selector",
            "should_expand_layered_bottom_sheet": 0,
            "is_from_lid_welcome_screen": 0,
            "device_id": data.android_id,
            "waterfall_id": data.waterfall_id,
            "INTERNAL__latency_qpl_instance_id": data.qpl_instance_id,
            "reg_flow_source": "login_home_native_integration_point",
            "is_caa_perf_enabled": 1,
            "is_platform_login": 0,
            "INTERNAL__latency_qpl_marker_id": data.qpl_marker_id,
            "family_device_id": "None",
            "offline_experiment_group": data.experiment_group,
            "entrypoint": "login_home_async",
            "access_flow_version": "pre_mt_behavior",
            "is_eligible_for_igds_sac_reg_flow": 0,
            "is_from_logged_in_switcher": 0,
            "qe_device_id": data.device_id,
        },
    }

    return {
        "method": "post",
        "pretty": "false",
        "format": "json",
        "server_timestamps": "true",
        "locale": "user",
        "purpose": "fetch",
        "fb_api_req_friendly_name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",
        "client_doc_id": "356548512614739681018024088968",
        "enable_canonical_naming": "true",
        "enable_canonical_variable_overrides": "true",
        "enable_canonical_naming_ambiguous_type_prefixing": "true",
        "variables": json.dumps(
            {
                "params": {
                    "params": json.dumps({"params": json.dumps(variables)})
                }
            }
        ),
    }


def register_click_headers(
    data: RegistrationData,
) -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        # 'Content-Length': '3139',
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data.user_agent,
        "X-Bloks-Version-Id": data.bloks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",  # don't know about this. Will generate and just pass
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data.app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data.android_id,
        "X-Ig-App-Id": data.app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data.device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data.zero_eh,  # when without login
        "X-Fb-Conn-Uuid-Client": "95b2bb513e6c590b7147b9e4bcf849d8",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }
