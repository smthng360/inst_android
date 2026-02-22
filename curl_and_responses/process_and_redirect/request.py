import os
import requests
from src.utils import write_response

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
    "X-Fb-Friendly-Name": "IgApi: bloks/async_action/com.bloks.www.bloks.caa.login.process_client_data_and_redirect/",
    "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"567067343352427","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
    "X-Fb-Server-Cluster": "True",
    "X-Ig-Android-Id": "android-fce52a1f75ffe4b9",
    "X-Ig-App-Id": "567067343352427",
    "X-Ig-App-Locale": "en_US",
    "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
    "X-Ig-Bandwidth-Totalbytes-B": "0",
    "X-Ig-Bandwidth-Totaltime-Ms": "0",
    "X-Ig-Client-Endpoint": "unknown",
    "X-Ig-Capabilities": "3brTv10=",
    "X-Ig-Connection-Type": "WIFI",
    "X-Ig-Device-Id": "0ebfd433-4663-481e-b1a3-367db479c3aa",
    "X-Ig-Device-Locale": "en_US",
    "X-Ig-Is-Foldable": "true",
    "X-Ig-Mapped-Locale": "en_US",
    "X-Ig-Timezone-Offset": "7200",
    "X-Ig-Www-Claim": "0",
    "X-Mid": "aV144QABAAEO9FyT3j05VsWnhwpt",
    "X-Pigeon-Rawclienttime": "1767733472.294",
    "X-Pigeon-Session-Id": "UFS-12ba6cab-3977-4d4a-9943-4b290413537d-0",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '1337',
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Fb-Conn-Uuid-Client": "cc800741f68a248aa8fa418ae85c54ee",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
}

data = {
    "params": '{"is_from_logged_out":false,"logged_out_user":"","qpl_join_id":"59d20075-93c8-427c-a78a-3196164cd15c","family_device_id":null,"device_id":"android-fce52a1f75ffe4b9","offline_experiment_group":"caa_iteration_v3_perf_ig_4","waterfall_id":"6c79c9de-55cc-4404-99d9-a88591831e9e","logout_source":"","show_internal_settings":false,"last_auto_login_time":0,"disable_auto_login":false,"qe_device_id":"0ebfd433-4663-481e-b1a3-367db479c3aa","use_auto_login_interstitial":true,"disable_recursive_auto_login_interstitial":true,"auto_login_interstitial_experiment_group_name":"","is_from_logged_in_switcher":false,"switcher_logged_in_uid":"","account_list":[],"blocked_uid":[],"INTERNAL_INFRA_THEME":"THREE_C","layered_homepage_experiment_group":"ld_no_language_selector","launched_url":"","sim_phone_numbers":[],"is_from_registration_reminder":false}',
    "bk_client_context": '{"bloks_version":"b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9","styles_id":"instagram"}',
    "bloks_versioning_id": "b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9",
}

response = requests.post(
    "https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.bloks.caa.login.process_client_data_and_redirect/",
    headers=headers,
    data=data,
    verify=False,
)

write_response(response, os.path.dirname(__file__))
