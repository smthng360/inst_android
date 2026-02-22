import os
from src.utils import write_response
import requests

headers = {
    "Host": "b.i.instagram.com",
    "Accept-Language": "en-US",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Ig-Intended-User-Id": "0",
    "Priority": "u=3",
    "X-Bloks-Is-Layout-Rtl": "false",
    "X-Bloks-Prism-Button-Version": "CONTROL",
    "X-Bloks-Prism-Colors-Enabled": "false",
    "X-Bloks-Prism-Extended-Palette-Gray": "false",
    "X-Bloks-Prism-Extended-Palette-Indigo": "false",
    "X-Bloks-Prism-Extended-Palette-Polish-Enabled": "false",
    "X-Bloks-Prism-Extended-Palette-Red": "false",
    "X-Bloks-Prism-Extended-Palette-Rest-Of-Colors": "false",
    "X-Bloks-Prism-Font-Enabled": "false",
    "X-Bloks-Prism-Indigo-Link-Version": "0",
    "X-Bloks-Version-Id": "b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Connection-Type": "WIFI",
    "X-Fb-Friendly-Name": "IgApi: bloks/async_action/com.bloks.www.bloks.caa.login.async.send_login_request/",
    "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"567067343352427","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
    "X-Fb-Server-Cluster": "True",
    "X-Ig-Android-Id": "android-f35f126bc4795e76",
    "X-Ig-App-Id": "567067343352427",
    "X-Ig-App-Locale": "en_US",
    "X-Ig-Attest-Params": '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"4rqaRd39DjXS865lAEHps1CQBnJmTkOx","signed_nonce":"","key_hash":""}]}',
    "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
    "X-Ig-Bandwidth-Totalbytes-B": "0",
    "X-Ig-Bandwidth-Totaltime-Ms": "0",
    "X-Ig-Client-Endpoint": "unknown",
    "X-Ig-Capabilities": "3brTv10=",
    "X-Ig-Connection-Type": "WIFI",
    "X-Ig-Device-Id": "941b3b2b-4663-46cc-bf7a-5e6da6c68528",
    "X-Ig-Device-Locale": "en_US",
    "X-Ig-Family-Device-Id": "966d2c83-fa78-4c3e-8fec-b51931833197",
    "X-Ig-Is-Foldable": "true",
    "X-Ig-Mapped-Locale": "en_US",
    "X-Ig-Timezone-Offset": "7200",
    "X-Ig-Www-Claim": "0",
    "X-Mid": "aW0HKwABAAEHIIUAyrJZZg-dH28v",
    "X-Pigeon-Rawclienttime": "1768752987.931",
    "X-Pigeon-Session-Id": "UFS-107db36b-e0f0-4f5e-8bb0-5506d103b806-0",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '3902',
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Fb-Conn-Uuid-Client": "3d6a0cfab8a6d0c79d645d6360c6135",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
}

data = {
    "params": '{"client_input_params":{"aac":"{\\"aac_init_timestamp\\":1768752939,\\"aacjid\\":\\"b7b91a3d-4152-40be-96cf-bbf7859dc755\\"}","sim_phones":[],"aymh_accounts":[],"network_bssid":null,"secure_family_device_id":"","has_granted_read_contacts_permissions":0,"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:4:1768752987:AZoxw0AwzvCT1cJOddcAAQUF2ZzeOJFPFAT097aroZb4dZvZfbpmUWgqGulJq4ycvFt1vRss6RvvIzZl0Plk092+BrJCNGUqX7RgboNgm3WfEARH0oawyze3WSzpGFpnYx22Lg/tldVFvHQQOwuIfybyp+SLHFHGV7RLJFR92ETkIlUaygDJuM/sO+Lh2TQNk5hh+R0Z2XKO61yqgyXFwYv8qJsJ3cNUMuxwvCyBKWJJuTTG2WWoR+24TcNKoKx8IVqbsiYbdkfSogyRHxfHcg+u+I1KYF2YSsyBD+7JxgblMCoXwPMBLpyNklOyPLpM6sEpJDiQw72N6nO7lyho85c4PqEa2dGKeSB2u0Q08uF6TXEeCIAjMqeHbI7TW1hMGNb6DjdSC1W/BWm8VdPRYVUmqinMZ+vG2DbNoWnNtQ==","sso_token_map_json_string":"","block_store_machine_id":"","ig_vetted_device_nonces":null,"cloud_trust_token":null,"event_flow":"login_manual","password_contains_non_ascii":"false","client_known_key_hash":"","encrypted_msisdn":"","has_granted_read_phone_permissions":0,"app_manager_id":"","should_show_nested_nta_from_aymh":0,"device_id":"android-f35f126bc4795e76","zero_balance_state":"","login_attempt_count":1,"machine_id":"aW0HKwABAAEHIIUAyrJZZg-dH28v","flash_call_permission_status":{"READ_PHONE_STATE":"DENIED","READ_CALL_LOG":"DENIED","ANSWER_PHONE_CALLS":"DENIED"},"accounts_list":[],"family_device_id":"966d2c83-fa78-4c3e-8fec-b51931833197","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":""},"event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"contact_point":"_.ringoo._"},"server_params":{"should_trigger_override_login_2fa_action":0,"is_vanilla_password_page_empty_password":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":"f32b1160-5921-462b-b1c6-c8ba94209e8d","two_step_login_type":"one_step_login","login_source":"Login","is_platform_login":0,"INTERNAL__latency_qpl_marker_id":36707139,"is_from_aymh":0,"offline_experiment_group":"caa_iteration_v3_perf_ig_4","is_from_landing_page":0,"left_nav_button_action":"NONE","password_text_input_id":"xtytiz:109","is_from_empty_password":0,"is_from_msplit_fallback":0,"ar_event_source":"login_home_page","qe_device_id":"941b3b2b-4663-46cc-bf7a-5e6da6c68528","username_text_input_id":"xtytiz:108","layered_homepage_experiment_group":"vanilla_ld","device_id":"android-f35f126bc4795e76","INTERNAL__latency_qpl_instance_id":2.04571724300364E14,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":null,"is_from_assistive_id":0,"access_flow_version":"pre_mt_behavior","is_from_logged_in_switcher":0}}',
    "bk_client_context": '{"bloks_version":"b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9","styles_id":"instagram"}',
    "bloks_versioning_id": "b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9",
}

response = requests.post(
    "https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.async.send_login_request/",
    headers=headers,
    data=data,
    verify=False,
)

write_response(response, os.path.dirname(__file__))
