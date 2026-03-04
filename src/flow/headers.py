import json

import typing

from ..schema import RegistrationData

if typing.TYPE_CHECKING:
    from .main import Flow
    from .registration import RegistrationFlow


def get_mobile_config_headers(
    blocks_version: str,
    app_id: str,
    device_id: str,
    user_agent: str,
    android_id: str,
    pigeon_raw_client_time: str,
    pigeon_session_id: str,
) -> dict:
    return {
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
        "X-Bloks-Version-Id": blocks_version,
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "IgApi: launcher/mobileconfig/sessionless",
        "X-Fb-Request-Analytics-Tags": json.dumps(
            {
                "network_tags": {
                    "product": app_id,
                    "surface": "undefined",
                    "request_category": "api",
                    "purpose": "fetch",
                    "retry_attempt": "0",
                }
            }
        ),
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": android_id,
        "X-Ig-App-Id": app_id,
        "X-Ig-App-Locale": "en_US",
        "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
        "X-Ig-Bandwidth-Totalbytes-B": "0",
        "X-Ig-Bandwidth-Totaltime-Ms": "0",
        "X-Ig-Client-Endpoint": "unknown",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Device-Id": device_id,
        "X-Ig-Device-Locale": "en_US",
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Mapped-Locale": "en_US",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Www-Claim": "0",
        "X-Pigeon-Rawclienttime": pigeon_raw_client_time,
        "X-Pigeon-Session-Id": pigeon_session_id,
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Content-Length': '509',
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "10af2f9d2692c905202c06f575140bd9",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    }


def get_dual_headers(
    blocks_version: str,
    device_id: str,
    user_agent: str,
    android_id: str,
    pigeon_raw_client_time: str,
    pigeon_session_id: str,
    app_id,
) -> dict:
    return {
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
        "X-Bloks-Version-Id": blocks_version,
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "IgApi: zr/dual_tokens/",
        "X-Fb-Request-Analytics-Tags": json.dumps(
            {
                "network_tags": {
                    "product": app_id,
                    "surface": "undefined",
                    "request_category": "api",
                    "purpose": "fetch",
                    "retry_attempt": "0",
                }
            }
        ),
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": android_id,
        "X-Ig-App-Id": app_id,
        "X-Ig-App-Locale": "en_US",
        "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
        "X-Ig-Bandwidth-Totalbytes-B": "0",
        "X-Ig-Bandwidth-Totaltime-Ms": "0",
        "X-Ig-Client-Endpoint": "unknown",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Device-Id": device_id,
        "X-Ig-Device-Locale": "en_US",
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Mapped-Locale": "en_US",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Www-Claim": "0",
        "X-Pigeon-Rawclienttime": pigeon_raw_client_time,
        "X-Pigeon-Session-Id": pigeon_session_id,
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Content-Length': '134',
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "cc800741f68a248aa8fa418ae85c54ee",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    }


def get_process_and_redirect_headers(
    blocks_version: str,
    app_id: str,
    device_id: str,
    user_agent: str,
    x_mid: str,
    android_id: str,
    pigeon_raw_client_time: str,
    pigeon_session_id: str,
) -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
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
        "X-Bloks-Version-Id": blocks_version,
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "IgApi: bloks/async_action/com.bloks.www.bloks.caa.login.process_client_data_and_redirect/",
        "X-Fb-Request-Analytics-Tags": json.dumps(
            {
                "network_tags": {
                    "product": app_id,
                    "surface": "undefined",
                    "request_category": "api",
                    "purpose": "fetch",
                    "retry_attempt": "0",
                }
            }
        ),
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": android_id,
        "X-Ig-App-Id": app_id,
        "X-Ig-App-Locale": "en_US",
        "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
        "X-Ig-Bandwidth-Totalbytes-B": "0",
        "X-Ig-Bandwidth-Totaltime-Ms": "0",
        "X-Ig-Client-Endpoint": "unknown",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Device-Id": device_id,
        "X-Ig-Device-Locale": "en_US",
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Mapped-Locale": "en_US",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Www-Claim": "0",
        "X-Mid": x_mid,
        "X-Pigeon-Rawclienttime": pigeon_raw_client_time,
        "X-Pigeon-Session-Id": pigeon_session_id,
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "cc800741f68a248aa8fa418ae85c54ee",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    }


def get_first_log_headers(app_id: str, user_agent: str):
    return {
        "Host": "z-p42.graph.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Priority": "u=5, i",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "undefined:analytics",
        "X-Fb-Request-Analytics-Tags": json.dumps(
            {
                "network_tags": {
                    "product": app_id,
                    "surface": "undefined",
                    "is_ad": "0",
                    "request_category": "analytics",
                    "purpose": "prefetch",
                    "retry_attempt": "0",
                }
            }
        ),
        "X-Fb-Server-Cluster": "True",
        "X-Ig-App-Id": app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Content-Length': '2259',
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "1fe53a462b93835b40bbeaad5e38c510",
        "X-Fb-Exp-Tag": "None,None,None",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "Connection": "keep-alive",
    }


def get_token_fetch_headers(
    blocks_version: str,
    app_id: str,
    device_id: str,
    user_agent: str,
    android_id: str,
    pigeon_raw_client_time: str,
    pigeon_session_id: str,
    family_device_id: str,
    x_mid: str,
) -> dict:
    return {
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
        "X-Bloks-Version-Id": blocks_version,
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "IgApi: bloks/async_action/com.bloks.www.caa.login.oauth.token.fetch.async/",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":'
        + app_id
        + ',"surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": android_id,
        "X-Ig-App-Id": app_id,
        "X-Ig-App-Locale": "en_US",
        "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
        "X-Ig-Bandwidth-Totalbytes-B": "0",
        "X-Ig-Bandwidth-Totaltime-Ms": "0",
        "X-Ig-Client-Endpoint": "unknown",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Device-Id": device_id,
        "X-Ig-Device-Locale": "en_US",
        "X-Ig-Family-Device-Id": family_device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Mapped-Locale": "en_US",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Www-Claim": "0",
        "X-Mid": x_mid,
        "X-Pigeon-Rawclienttime": pigeon_raw_client_time,
        "X-Pigeon-Session-Id": pigeon_session_id,
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Content-Length': '1226',
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "3d6a0cfab8a6d0c79d645d6360c6135",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    }


def get_create_keystore_headers(
    blocks_version: str,
    app_id: str,
    device_id: str,
    user_agent: str,
    android_id: str,
    pigeon_raw_client_time: str,
    pigeon_session_id: str,
) -> dict:
    return {
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
        "X-Bloks-Version-Id": blocks_version,
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "IgApi: attestation/create_android_keystore/",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + app_id
        + '","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": android_id,
        "X-Ig-App-Id": app_id,
        "X-Ig-App-Locale": "en_US",
        "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
        "X-Ig-Bandwidth-Totalbytes-B": "0",
        "X-Ig-Bandwidth-Totaltime-Ms": "0",
        "X-Ig-Client-Endpoint": "unknown",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Device-Id": device_id,
        "X-Ig-Device-Locale": "en_US",
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Mapped-Locale": "en_US",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Www-Claim": "0",
        "X-Pigeon-Rawclienttime": pigeon_raw_client_time,
        "X-Pigeon-Session-Id": pigeon_session_id,
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "54cb3412e733a34fd05f0353ea3872ea",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    }


def get_send_login_headers(
    blocks_version: str,
    app_id: str,
    device_id: str,
    user_agent: str,
    android_id: str,
    family_device_id: str,
    pigeon_raw_client_time: str,
    pigeon_session_id: str,
    x_mid: str,
    challenge_nonce: str,
) -> dict:
    return {
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
        "X-Bloks-Version-Id": blocks_version,
        "X-Fb-Client-Ip": "True",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Friendly-Name": "IgApi: bloks/async_action/com.bloks.www.bloks.caa.login.async.send_login_request/",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + app_id
        + '","surface":"undefined","request_category":"api","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": android_id,
        "X-Ig-App-Id": app_id,
        "X-Ig-App-Locale": "en_US",
        "X-Ig-Attest-Params": '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"'
        + challenge_nonce
        + '","signed_nonce":"","key_hash":""}]}',
        "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
        "X-Ig-Bandwidth-Totalbytes-B": "0",
        "X-Ig-Bandwidth-Totaltime-Ms": "0",
        "X-Ig-Client-Endpoint": "unknown",
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Device-Id": device_id,
        "X-Ig-Device-Locale": "en_US",
        "X-Ig-Family-Device-Id": family_device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Mapped-Locale": "en_US",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Www-Claim": "0",
        "X-Mid": x_mid,
        "X-Pigeon-Rawclienttime": pigeon_raw_client_time,
        "X-Pigeon-Session-Id": pigeon_session_id,
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
        "User-Agent": user_agent,
        "X-Fb-Conn-Uuid-Client": "3d6a0cfab8a6d0c79d645d6360c6135",
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    }


def get_register_click_headers(
    data: "RegistrationFlow",
) -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",  # don't know about this. Will generate and just pass
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.aymh_create_account_button.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,  # also checck this for generation
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_phone_request_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        # 'Content-Length': '27226',
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "253360298312778871684788706414",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.contactpoint_phone",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_app",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_email_button_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "253360298312778871684788706414",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.contactpoint_email",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_app",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_email_submit_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_confirmation_request_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.confirmation.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "false",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_password_create_headers(data: "RegistrationFlow"):
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        # 'Content-Length': '30283',
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.password.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        # 'Accept-Encoding': 'gzip, deflate, br',
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_birth_headers(data: "RegistrationFlow"):
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        # 'Content-Length': '30274',
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.birthday.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        # 'Accept-Encoding': 'gzip, deflate, br',
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_name_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        # 'Content-Length': '30216',
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.name_ig_and_soap.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        # 'Accept-Encoding': 'gzip, deflate, br',
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_agreement_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.create.account.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Attest-Params": json.dumps({"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":data._challenge_nonce,"signed_nonce":"","key_hash":""},{"version":3,"type":"play_integrity","errors":[-9],"challenge_nonce":data._challenge_nonce_2,"integrity_token":""}]}, separators=(',', ':')),
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "false",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        'Accept-Encoding': 'gzip, deflate, br',
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


def get_username_headers(data: "RegistrationFlow") -> dict:
    return {
        "Host": "b.i.instagram.com",
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded",
        "Priority": "u=3, i",
        "User-Agent": data._user_agent,
        "X-Bloks-Version-Id": data._blocks_version,
        "X-Client-Doc-Id": "356548512614739681018024088968",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Friendly-Name": "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.username.async",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"'
        + data._app_id
        + '","request_category":"graphql","purpose":"fetch","retry_attempt":"0"}}',
        "X-Fb-Server-Cluster": "True",
        "X-Ig-Android-Id": data._android_id,
        "X-Ig-App-Id": data._app_id,
        "X-Ig-Capabilities": "3brTv10=",
        "X-Ig-Device-Id": data._device_id,
        "X-Ig-Is-Foldable": "true",
        "X-Ig-Timezone-Offset": "7200",
        "X-Ig-Validate-Null-In-Legacy-Dict": "true",
        "X-Root-Field-Name": "bloks_action",
        "X-Tigon-Is-Retry": "False",
        "X-Zero-Eh": data._zero_eh,
        # 'Accept-Encoding': 'gzip, deflate, br',
        "X-Fb-Conn-Uuid-Client": data._conn_uuid_client,
        "X-Fb-Http-Engine": "Tigon/MNS/TCP",
        "X-Graphql-Client-Library": "pando",
        "X-Graphql-Request-Purpose": "fetch",
    }


