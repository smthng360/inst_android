import requests
import os
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
    "X-Fb-Friendly-Name": "IgApi: bloks/async_action/com.bloks.www.caa.login.oauth.token.fetch.async/",
    "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"567067343352427","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
    "X-Fb-Server-Cluster": "True",
    "X-Ig-Android-Id": "android-fce52a1f75ffe4b9",
    "X-Ig-App-Id": "567067343352427",
    "X-Ig-App-Locale": "en_US",
    "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
    "X-Ig-Bandwidth-Totalbytes-B": "0",
    "X-Ig-Bandwidth-Totaltime-Ms": "0",
    "X-Ig-Client-Endpoint": "com.bloks.www.caa.login.login_homepage:com.bloks.www.caa.login.login_homepage",
    "X-Ig-Capabilities": "3brTv10=",
    "X-Ig-Connection-Type": "WIFI",
    "X-Ig-Device-Id": "ee5996a3-4663-49d9-a2a9-bc5ce2f66c85",
    "X-Ig-Device-Locale": "en_US",
    "X-Ig-Family-Device-Id": "6b6bb097-d464-47cb-8c05-6852adc00186",
    "X-Ig-Is-Foldable": "true",
    "X-Ig-Mapped-Locale": "en_US",
    "X-Ig-Nav-Chain": "com.bloks.www.caa.login.login_homepage:com.bloks.www.caa.login.login_homepage:1:button:1768330504.310::",
    "X-Ig-Timezone-Offset": "7200",
    "X-Ig-Www-Claim": "0",
    "X-Mid": "aWaVKwABAAF0PwvsdbGRkfg3BxAO",
    "X-Pigeon-Rawclienttime": "1768330541.615",
    "X-Pigeon-Session-Id": "UFS-d7743010-4089-4e61-90a1-491c5b0c000c-0",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '1171',
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Fb-Conn-Uuid-Client": "3fa53dfdfe2de942f413b8f36be493ec",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
}

data = {
    "params": '{"client_input_params":{"username_input":"_.ringoo._","aac":"{\\"aac_init_timestamp\\":1768330539}","lois_settings":{"lois_token":""},"zero_balance_state":"","network_bssid":null},"server_params":{"is_from_logged_out":0,"layered_homepage_experiment_group":"Deploy: Not in Experiment","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"device_id":"android-fce52a1f75ffe4b9","offline_experiment_group":"caa_iteration_v3_perf_ig_4","waterfall_id":"5d573515-3755-444f-9c93-ba46ff948219","access_flow_version":"pre_mt_behavior","INTERNAL__latency_qpl_instance_id":2.07678418700091E14,"is_from_logged_in_switcher":0,"is_platform_login":0,"qe_device_id":"ee5996a3-4663-49d9-a2a9-bc5ce2f66c85"}}',
    "bk_client_context": '{"bloks_version":"b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9","styles_id":"instagram"}',
    "bloks_versioning_id": "b7737193b91c3a2f4050bdfc9d9ae0f578a93b4181fd43efe549daacba5c7db9",
}

response = requests.post(
    "https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.login.oauth.token.fetch.async/",
    headers=headers,
    data=data,
    verify=False,
)

write_response(response, os.path.dirname(__file__))
