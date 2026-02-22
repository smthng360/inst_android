from pydantic import BaseModel, Field
from typing import Any, List
from enum import StrEnum


class InputIds(BaseModel):
    username_id: str
    password_id: str


class RegistrationDict(BaseModel):
    first_name: str | None
    last_name: str | None
    full_name: str | None
    contactpoint: Any
    ar_contactpoint: Any
    contactpoint_type: Any
    is_using_unified_cp: Any
    unified_cp_screen_variant: str
    is_cp_auto_confirmed: bool
    is_cp_auto_confirmable: bool
    is_cp_claimed: bool
    confirmation_code: Any
    birthday: Any
    birthday_derived_from_age: Any
    age_range: Any
    did_use_age: Any
    os_shared_age_range: Any
    gender: Any
    use_custom_gender: bool
    custom_gender: Any
    encrypted_password: Any
    username: Any
    username_prefill: Any
    fb_conf_source: Any
    device_id: str
    ig4a_qe_device_id: str
    family_device_id: Any
    user_id: Any
    safetynet_token: Any
    skip_slow_rel_check: bool
    safetynet_response: Any
    machine_id: str
    profile_photo: Any
    profile_photo_id: Any
    profile_photo_upload_id: Any
    avatar: Any
    email_oauth_token_no_contact_perm: Any
    email_oauth_token: Any
    email_oauth_tokens: Any
    sign_in_with_google_email: Any
    should_skip_two_step_conf: Any
    openid_tokens_for_testing: Any
    encrypted_msisdn: Any
    encrypted_msisdn_for_safetynet: Any
    cached_headers_safetynet_info: Any
    should_skip_headers_safetynet: Any
    headers_last_infra_flow_id: Any
    headers_last_infra_flow_id_safetynet: Any
    headers_flow_id: Any
    was_headers_prefill_available: Any
    sso_enabled: Any
    existing_accounts: Any
    used_ig_birthday: Any
    create_new_to_app_account: Any
    skip_session_info: Any
    ck_error: Any
    ck_id: Any
    ck_nonce: Any
    should_save_password: Any
    fb_access_token: Any
    is_msplit_reg: Any
    is_spectra_reg: Any
    dema_account_consent_given: Any
    spectra_reg_token: Any
    spectra_reg_guardian_id: Any
    spectra_reg_guardian_logged_in_context: Any
    user_id_of_msplit_creator: Any
    msplit_creator_nonce: Any
    dma_data_combination_consent_given: Any
    xapp_accounts: Any
    fb_device_id: Any
    fb_machine_id: Any
    ig_device_id: Any
    ig_machine_id: Any
    should_skip_nta_upsell: Any
    big_blue_token: Any
    caa_reg_flow_source: str
    ig_authorization_token: Any
    full_sheet_flow: bool
    crypted_user_id: Any
    is_caa_perf_enabled: bool
    is_preform: bool
    should_show_rel_error: bool
    ignore_suma_check: bool
    dismissed_login_upsell_with_cna: bool
    ignore_existing_login: bool
    ignore_existing_login_from_suma: bool
    ignore_existing_login_after_errors: bool
    suggested_first_name: Any
    suggested_last_name: Any
    suggested_full_name: Any
    frl_authorization_token: Any
    post_form_errors: Any
    skip_step_without_errors: bool
    existing_account_exact_match_checked: bool
    existing_account_fuzzy_match_checked: bool
    email_oauth_exists: bool
    confirmation_code_send_error: Any
    is_too_young: bool
    source_account_type: Any
    whatsapp_installed_on_client: bool
    confirmation_medium: Any
    source_credentials_type: Any
    source_cuid: Any
    source_account_reg_info: Any
    soap_creation_source: Any
    source_account_type_to_reg_info: Any
    registration_flow_id: str
    should_skip_youth_tos: bool
    is_youth_regulation_flow_complete: bool
    is_on_cold_start: bool
    email_prefilled: bool
    cp_confirmed_by_auto_conf: bool
    in_sowa_experiment: bool
    youth_regulation_config: Any
    conf_allow_back_nav_after_change_cp: Any
    conf_bouncing_cliff_screen_type: Any
    conf_show_bouncing_cliff: Any
    eligible_to_flash_call_in_ig4a: bool
    eligible_to_mo_sms_in_ig4a: bool
    mo_sms_ent_id: Any
    flash_call_permissions_status: Any
    gms_incoming_call_retriever_eligibility: Any
    attestation_result: Any
    request_data_and_challenge_nonce_string: Any
    confirmed_cp_and_code: Any
    notification_callback_id: Any
    reg_suma_state: int
    is_msplit_neutral_choice: bool
    msg_previous_cp: Any
    ntp_import_source_info: Any
    youth_consent_decision_time: Any
    should_show_spi_before_conf: bool
    google_oauth_account: Any
    is_reg_request_from_ig_suma: bool
    is_toa_reg: bool
    is_threads_public: bool
    spc_import_flow: bool
    caa_play_integrity_attestation_result: Any
    client_known_key_hash: Any
    flash_call_provider: Any
    spc_birthday_input: bool
    failed_birthday_year_count: Any
    user_presented_medium_source: Any
    user_opted_out_of_ntp: Any
    is_from_registration_reminder: bool
    show_youth_reg_in_ig_spc: bool
    fb_suma_is_high_confidence: Any
    screen_visited: List
    fb_email_login_upsell_skip_suma_post_tos: bool
    fb_suma_is_from_email_login_upsell: bool
    fb_suma_is_from_phone_login_upsell: bool
    should_prefill_cp_in_ar: Any
    ig_partially_created_account_user_id: Any
    ig_partially_created_account_nonce: Any
    ig_partially_created_account_nonce_expiry: Any
    force_sessionless_nux_experience: bool
    has_seen_suma_landing_page_pre_conf: bool
    has_seen_suma_candidate_page_pre_conf: bool
    suma_on_conf_threshold: int
    move_suma_to_cp_variant: str
    pp_to_nux_eligible: bool
    should_show_error_msg: bool
    th_profile_photo_token: Any
    attempted_silent_auth_in_fb: bool
    attempted_silent_auth_in_ig: bool
    cp_suma_results_map: Any
    source_username: Any
    next_uri: Any
    should_use_next_uri: Any
    linking_entry_point: Any
    fb_encrypted_partial_new_account_properties: Any
    starter_pack_name: Any
    starter_pack_creator_user_ids: Any
    wa_data_bundle: Any
    bloks_controller_source: Any
    airwave_registration_code: Any
    is_sessionless_nux: Any
    login_contactpoint: Any
    login_contactpoint_type: Any
    is_nta_shortened: bool
    should_show_bday_after_name_suggestions: Any
    should_override_back_nav: bool
    ig_footer_variant: str
    device_network_info: Any
    is_from_web_lite_reg_controller: Any
    login_form_siwg_email: Any
    account_setup_waterfall_id: Any
    is_wanted_suma_user: bool
    device_zero_balance_state: Any


class BloksPayloadType(StrEnum):
    APP = "app"
    ACTION = "action"


class EmailAccount(BaseModel):
    email: str = Field(..., alias="Email")
    password: str = Field(..., alias="Password")
    refresh_token: str = Field(..., alias="RefreshToken")
    access_token: str | None = Field(None, alias="AccessToken")
    r_expire: str | None = Field(None, alias="R_Expire")
    client_id: str | None = Field(None, alias="ClientId")
