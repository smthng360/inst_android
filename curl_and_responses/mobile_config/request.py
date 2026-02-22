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
    "X-Fb-Friendly-Name": "IgApi: launcher/mobileconfig/sessionless",
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
    "X-Pigeon-Rawclienttime": "1767733471.735",
    "X-Pigeon-Session-Id": "UFS-12ba6cab-3977-4d4a-9943-4b290413537d-0",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '509',
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Fb-Conn-Uuid-Client": "10af2f9d2692c905202c06f575140bd9",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
}

data = {
    "signed_body": 'SIGNATURE.{"bool_opt_policy":"0","mobileconfigsessionless":"","api_version":"10","unit_type":"1","use_case":"STANDARD","query_hash":"3dda1251bd0edfd452095e7d3eb3c040f2513628cbded5de8031c732652ef7f6","tier":"-1","device_id":"0ebfd433-4663-481e-b1a3-367db479c3aa","fetch_mode":"CONFIG_SYNC_ONLY","fetch_type":"SYNC_FULL","family_device_id":"EMPTY_FAMILY_DEVICE_ID"}',
}

response = requests.post(
    "https://b.i.instagram.com/api/v1/launcher/mobileconfig/",
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)
