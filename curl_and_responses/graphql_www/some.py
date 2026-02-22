import requests
from src.utils import write_response
import os


headers = {
    "Host": "i.instagram.com",
    "Accept-Language": "en-US",
    # 'Content-Length': '3198',
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
    "X-Ig-Device-Id": "03215fdb-3663-446a-85cc-79b3af3b1273",
    "X-Ig-Is-Foldable": "true",
    "X-Ig-Timezone-Offset": "7200",
    "X-Ig-Validate-Null-In-Legacy-Dict": "true",
    "X-Root-Field-Name": "bloks_action",
    "X-Tigon-Is-Retry": "False",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "X-Fb-Conn-Uuid-Client": "7cc09d99a565c06699f629e4f19cdc7",
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
    "variables": '{"params":{"params":"{\\"params\\":\\"{\\\\\\"client_input_params\\\\\\":{\\\\\\"should_show_nested_nta_bottom_sheet\\\\\\":0,\\\\\\"accounts_list\\\\\\":[],\\\\\\"username_input\\\\\\":\\\\\\"\\\\\\",\\\\\\"aac\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"aac_init_timestamp\\\\\\\\\\\\\\":1769024773,\\\\\\\\\\\\\\"aacjid\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"c2e658b9-d01d-4970-b3ba-268fc0ad5859\\\\\\\\\\\\\\"}\\\\\\",\\\\\\"device_emails\\\\\\":[],\\\\\\"lois_settings\\\\\\":{\\\\\\"lois_token\\\\\\":\\\\\\"\\\\\\"},\\\\\\"zero_balance_state\\\\\\":\\\\\\"\\\\\\",\\\\\\"network_bssid\\\\\\":null,\\\\\\"device_phone_numbers\\\\\\":[]},\\\\\\"server_params\\\\\\":{\\\\\\"is_from_logged_out\\\\\\":0,\\\\\\"layered_homepage_experiment_group\\\\\\":\\\\\\"Deploy: Not in Experiment\\\\\\",\\\\\\"should_expand_layered_bottom_sheet\\\\\\":0,\\\\\\"is_from_lid_welcome_screen\\\\\\":0,\\\\\\"device_id\\\\\\":\\\\\\"android-f35f126bc4795e76\\\\\\",\\\\\\"waterfall_id\\\\\\":\\\\\\"b840d71d-9a93-4090-94cf-06518ab90106\\\\\\",\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\":9.4784122800432E13,\\\\\\"reg_flow_source\\\\\\":\\\\\\"login_home_native_integration_point\\\\\\",\\\\\\"is_caa_perf_enabled\\\\\\":1,\\\\\\"is_platform_login\\\\\\":0,\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\":36707139,\\\\\\"family_device_id\\\\\\":\\\\\\"d9c7a206-bcdd-41a3-89f1-273e46af327a\\\\\\",\\\\\\"offline_experiment_group\\\\\\":\\\\\\"caa_iteration_v3_perf_ig_4\\\\\\",\\\\\\"entrypoint\\\\\\":\\\\\\"login_home_async\\\\\\",\\\\\\"access_flow_version\\\\\\":\\\\\\"pre_mt_behavior\\\\\\",\\\\\\"is_eligible_for_igds_sac_reg_flow\\\\\\":0,\\\\\\"is_from_logged_in_switcher\\\\\\":0,\\\\\\"qe_device_id\\\\\\":\\\\\\"03215fdb-3663-446a-85cc-79b3af3b1273\\\\\\"}}\\"}","bloks_versioning_id":"b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9","infra_params":{"device_id":"03215fdb-3663-446a-85cc-79b3af3b1273"},"app_id":"com.bloks.www.bloks.caa.reg.aymh_create_account_button.async"},"bk_context":{"is_flipper_enabled":false,"theme_params":[],"debug_tooling_metadata_token":null}}',
}

response = requests.post(
    "https://i.instagram.com/graphql_www",
    headers=headers,
    data=data,
    verify=False,
)


write_response(response, os.path.dirname(__file__))
