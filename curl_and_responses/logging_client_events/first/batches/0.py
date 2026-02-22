import random
from typing import Dict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.flow.main import Flow


def build_first_log(base_time: float, flow: "Flow") -> Dict:
    """
    base_time: Unix timestamp in seconds (float or int)
    """

    app_id = flow._app_id
    app_ver = flow._picked_instagram_version
    build_num = 846519343
    device = "sdk_gphone64_arm64"
    os_ver = "12"
    device_id = flow._device_id
    pigeon_session_id = flow._pigeon_session_id
    waterfall_id = flow._waterfall_id

    batch_time_ms = int(base_time * 1000)
    start_time_ms = batch_time_ms - random.randint(350, 650)

    def event_time(delta_ms: int):
        current = start_time_ms + delta_ms
        return {
            "start_time": float(start_time_ms),
            "current_time": float(current),
            "elapsed_time": float(current - start_time_ms),
            "event_time_sec": current / 1000,
        }

    e1 = event_time(485)
    e2 = event_time(485)
    e3 = event_time(561)

    return {
        "batches": [
            {
                "time": batch_time_ms,
                "app_id": app_id,
                "app_ver": app_ver,
                "build_num": build_num,
                "consent_state": 0,
                "device": device,
                "os_ver": os_ver,
                "device_id": device_id,
                "session_id": pigeon_session_id,
                "seq": 2,
                "app_uid": "0",
                "data": [
                    {
                        "extra": {
                            "waterfall_id": waterfall_id,
                            "experiment": "ig4a_layered_design_activity_experiment",
                            "test_group": "ld_no_language_selector",
                            "guid": device_id,
                            "containermodule": "waterfall_log_in",
                            "elapsed_time": e1["elapsed_time"],
                            "start_time": e1["start_time"],
                            "current_time": e1["current_time"],
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -2.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": e1["event_time_sec"],
                        "name": "ig_local_exposure",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "exp_name": "ig4a_layered_design_activity_experiment",
                            "exp_group": "ld_no_language_selector",
                            "app_device_id": device_id,
                            "containermodule": "waterfall_log_in",
                            "elapsed_time": e2["elapsed_time"],
                            "start_time": e2["start_time"],
                            "current_time": e2["current_time"],
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -2.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": e2["event_time_sec"],
                        "name": "initial_app_launch_experiment_exposure",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "current_time": e3["current_time"],
                            "elapsed_time": e3["elapsed_time"],
                            "flow": "LOG_IN",
                            "start_time": e3["start_time"],
                            "waterfall_id": waterfall_id,
                            "containermodule": "waterfall_log_in",
                            "api_level": 31,
                            "guid": device_id,
                            "source": None,
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": e3["event_time_sec"],
                        "name": "get_google_account_attempt",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                ],
            },
            {
                "time": 1767733471404,
                "app_id": app_id,
                "app_ver": app_ver,
                "build_num": build_num,
                "consent_state": 0,
                "device": "sdk_gphone64_arm64",
                "os_ver": "12",
                "device_id": device_id,
                "device_id": pigeon_session_id,
                "seq": 1,
                "app_uid": "0",
                "data": [
                    {
                        "extra": {
                            "marker_id": 27792138,
                            "instance_id": 1035897792,
                            "sample_rate": 1,
                            "sample_source": 3,
                            "time_since_boot_ms": random.randint(
                                300_000_000, 380_000_000
                            ),
                            "duration_ns": 0,
                            "action_id": 0,
                            "marker_type": 1,
                            "method": "random_sampling",
                            "da_level": 7,
                            "da_type": "app_init",
                            "annotations_bool": {
                                "qpl_internal__missing_config_tracker_enabled": False
                            },
                            "marker": "client_tti",
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(base_time - random.uniform(0.55, 0.6), 3),
                        "name": "perf",
                        "sampling_rate": 1,
                        "tags": 8388608,
                    }
                ],
            },
            {
                "time": 1767733471393,
                "app_id": app_id,
                "app_ver": app_ver,
                "build_num": build_num,
                "consent_state": 0,
                "device": "sdk_gphone64_arm64",
                "os_ver": "12",
                "device_id": device_id,
                "device_id": pigeon_session_id,
                "seq": 0,
                "app_uid": "0",
                "data": [
                    {
                        "extra": {
                            "app_device_id": device_id,
                            "analytics_device_id": None,
                            "module": "instagram_device_ids",
                            "waterfall_id": waterfall_id,
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(
                            base_time - random.uniform(0.45, 0.55), 3
                        ),
                        "name": "instagram_device_ids",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "build_num": 846519343,
                            "installer": "com.google.android.packageinstaller",
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(base_time - random.uniform(0.4, 0.45), 3),
                        "name": "android_apk_testing_exposure",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "pigeon_reserved_keyword_module": "IgResourcesAnalyticsModule",
                            "app_locale": "en_US",
                            "client_string_id": "2131966674",
                            "device_locale": "en_US",
                            "requested_locale": "en",
                            "requested_fb_locale": "en_US",
                            "translation_bundle_type": "frsc",
                            "logger_version": 0,
                            "logger_name": "FbtLoggerImpl",
                            "requested_variations": [0, 0],
                            "are_downloadable_strings_disabled": False,
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(base_time - random.uniform(0.3, 0.4), 3),
                        "module": "IgResourcesAnalyticsModule",
                        "name": "intl_android_string_impressions",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "pigeon_reserved_keyword_module": "IgResourcesAnalyticsModule",
                            "app_locale": "en_US",
                            "client_string_id": "2131966682",
                            "device_locale": "en_US",
                            "requested_locale": "en",
                            "requested_fb_locale": "en_US",
                            "translation_bundle_type": "frsc",
                            "logger_version": 0,
                            "logger_name": "FbtLoggerImpl",
                            "requested_variations": [0, 0],
                            "are_downloadable_strings_disabled": False,
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(base_time - random.uniform(0.2, 0.3), 3),
                        "module": "IgResourcesAnalyticsModule",
                        "name": "intl_android_string_impressions",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "pigeon_reserved_keyword_module": "IgResourcesAnalyticsModule",
                            "app_locale": "en_US",
                            "client_string_id": "2131966674",
                            "device_locale": "en_US",
                            "requested_locale": "en",
                            "requested_fb_locale": "en_US",
                            "translation_bundle_type": "frsc",
                            "logger_version": 0,
                            "logger_name": "FbtLoggerImpl",
                            "requested_variations": [0, 0],
                            "are_downloadable_strings_disabled": False,
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(base_time - random.uniform(0.15, 0.2), 3),
                        "module": "IgResourcesAnalyticsModule",
                        "name": "intl_android_string_impressions",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                    {
                        "extra": {
                            "pigeon_reserved_keyword_module": "IgResourcesAnalyticsModule",
                            "app_locale": "en_US",
                            "client_string_id": "2131966682",
                            "device_locale": "en_US",
                            "requested_locale": "en",
                            "requested_fb_locale": "en_US",
                            "translation_bundle_type": "frsc",
                            "logger_version": 0,
                            "logger_name": "FbtLoggerImpl",
                            "requested_variations": [0, 0],
                            "are_downloadable_strings_disabled": False,
                            "pk": "0",
                            "release_channel": "prod",
                            "radio_type": "WIFI-UNKNOWN",
                            "pigeon_reserved_keyword_requested_latency": -1.0,
                            "pigeon_reserved_keyword_log_type": "client_event",
                            "pigeon_reserved_keyword_bg": "true",
                        },
                        "log_type": "client_event",
                        "bg": "true",
                        "time": round(base_time - random.uniform(0.15, 0.2), 3),
                        "module": "IgResourcesAnalyticsModule",
                        "name": "intl_android_string_impressions",
                        "sampling_rate": 1,
                        "tags": 8388609,
                    },
                ],
            },
        ],
        "request_info": {
            "tier": "micro_batch",
            "sent_time": round(base_time + random.uniform(0.02, 0.05), 3),
            "carrier": "T-Mobile",
            "conn": "WIFI",
        },
        "config": {
            "config_checksum": None,
            "config_version": "v2",
            "qpl_config_version": "v7",
            "app_ver": app_ver,
            "app_uid": "0",
        },
    }
