# -*- coding: utf-8 -*-
#
from ..const import CONFIG

# Storage settings
COMMAND_STORAGE = {
    'ENGINE': 'terminal.backends.command.db',
}
DEFAULT_TERMINAL_COMMAND_STORAGE = {
    "default": {
        "TYPE": "server",
    },
}
TERMINAL_COMMAND_STORAGE = CONFIG.TERMINAL_COMMAND_STORAGE or {}

# Server 类型的录像存储
SERVER_REPLAY_STORAGE = CONFIG.SERVER_REPLAY_STORAGE
# SERVER_REPLAY_STORAGE = {
#     'TYPE': 's3',
#     'BUCKET': '',
#     'ACCESS_KEY': '',
#     'SECRET_KEY': '',
#     'ENDPOINT': ''
# }

DEFAULT_TERMINAL_REPLAY_STORAGE = {
    "default": {
        "TYPE": "server",
    },
}
TERMINAL_REPLAY_STORAGE = CONFIG.TERMINAL_REPLAY_STORAGE
FTP_FILE_MAX_STORE = CONFIG.FTP_FILE_MAX_STORE

# Security settings
SECURITY_MFA_AUTH = CONFIG.SECURITY_MFA_AUTH
SECURITY_MFA_AUTH_ENABLED_FOR_THIRD_PARTY = CONFIG.SECURITY_MFA_AUTH_ENABLED_FOR_THIRD_PARTY
SECURITY_MAX_IDLE_TIME = CONFIG.SECURITY_MAX_IDLE_TIME  # Unit: minute
SECURITY_MAX_SESSION_TIME = CONFIG.SECURITY_MAX_SESSION_TIME  # Unit: hour
SECURITY_COMMAND_EXECUTION = CONFIG.SECURITY_COMMAND_EXECUTION
SECURITY_COMMAND_BLACKLIST = CONFIG.SECURITY_COMMAND_BLACKLIST
SECURITY_PASSWORD_EXPIRATION_TIME = CONFIG.SECURITY_PASSWORD_EXPIRATION_TIME  # Unit: day
SECURITY_PASSWORD_MIN_LENGTH = CONFIG.SECURITY_PASSWORD_MIN_LENGTH  # Unit: bit
SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH = CONFIG.SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH  # Unit: bit
OLD_PASSWORD_HISTORY_LIMIT_COUNT = CONFIG.OLD_PASSWORD_HISTORY_LIMIT_COUNT
SECURITY_PASSWORD_UPPER_CASE = CONFIG.SECURITY_PASSWORD_UPPER_CASE
SECURITY_PASSWORD_LOWER_CASE = CONFIG.SECURITY_PASSWORD_LOWER_CASE
SECURITY_PASSWORD_NUMBER = CONFIG.SECURITY_PASSWORD_NUMBER
SECURITY_PASSWORD_SPECIAL_CHAR = CONFIG.SECURITY_PASSWORD_SPECIAL_CHAR
SECURITY_PASSWORD_RULES = [
    'SECURITY_PASSWORD_MIN_LENGTH',
    'SECURITY_PASSWORD_UPPER_CASE',
    'SECURITY_PASSWORD_LOWER_CASE',
    'SECURITY_PASSWORD_NUMBER',
    'SECURITY_PASSWORD_SPECIAL_CHAR'
]
VERIFY_CODE_TTL = CONFIG.VERIFY_CODE_TTL
SECURITY_MFA_VERIFY_TTL = CONFIG.SECURITY_MFA_VERIFY_TTL
SECURITY_UNCOMMON_USERS_TTL = CONFIG.SECURITY_UNCOMMON_USERS_TTL
SECURITY_VIEW_AUTH_NEED_MFA = CONFIG.SECURITY_VIEW_AUTH_NEED_MFA
SECURITY_SERVICE_ACCOUNT_REGISTRATION = CONFIG.SECURITY_SERVICE_ACCOUNT_REGISTRATION
SECURITY_LOGIN_CAPTCHA_ENABLED = CONFIG.SECURITY_LOGIN_CAPTCHA_ENABLED
SECURITY_MFA_IN_LOGIN_PAGE = CONFIG.SECURITY_MFA_IN_LOGIN_PAGE
SECURITY_LOGIN_CHALLENGE_ENABLED = CONFIG.SECURITY_LOGIN_CHALLENGE_ENABLED
SECURITY_DATA_CRYPTO_ALGO = CONFIG.SECURITY_DATA_CRYPTO_ALGO
SECURITY_INSECURE_COMMAND = CONFIG.SECURITY_INSECURE_COMMAND
SECURITY_INSECURE_COMMAND_LEVEL = CONFIG.SECURITY_INSECURE_COMMAND_LEVEL
SECURITY_INSECURE_COMMAND_EMAIL_RECEIVER = CONFIG.SECURITY_INSECURE_COMMAND_EMAIL_RECEIVER
SECURITY_CHECK_DIFFERENT_CITY_LOGIN = CONFIG.SECURITY_CHECK_DIFFERENT_CITY_LOGIN
# 用户登录限制的规则
SECURITY_LOGIN_LIMIT_COUNT = CONFIG.SECURITY_LOGIN_LIMIT_COUNT
SECURITY_LOGIN_LIMIT_TIME = CONFIG.SECURITY_LOGIN_LIMIT_TIME  # Unit: minute
# 登录IP限制的规则
SECURITY_LOGIN_IP_BLACK_LIST = CONFIG.SECURITY_LOGIN_IP_BLACK_LIST
SECURITY_LOGIN_IP_WHITE_LIST = CONFIG.SECURITY_LOGIN_IP_WHITE_LIST
SECURITY_LOGIN_IP_LIMIT_COUNT = CONFIG.SECURITY_LOGIN_IP_LIMIT_COUNT
SECURITY_LOGIN_IP_LIMIT_TIME = CONFIG.SECURITY_LOGIN_IP_LIMIT_TIME  # Unit: minute

# Authentication settings
# 缓存后可以给账号使用
CACHE_LOGIN_PASSWORD_ENABLED = CONFIG.CACHE_LOGIN_PASSWORD_ENABLED
CACHE_LOGIN_PASSWORD_TTL = CONFIG.CACHE_LOGIN_PASSWORD_TTL

# Terminal other setting
TERMINAL_PASSWORD_AUTH = CONFIG.TERMINAL_PASSWORD_AUTH
TERMINAL_PUBLIC_KEY_AUTH = CONFIG.TERMINAL_PUBLIC_KEY_AUTH
TERMINAL_HEARTBEAT_INTERVAL = CONFIG.TERMINAL_HEARTBEAT_INTERVAL
TERMINAL_ASSET_LIST_SORT_BY = CONFIG.TERMINAL_ASSET_LIST_SORT_BY
TERMINAL_ASSET_LIST_PAGE_SIZE = CONFIG.TERMINAL_ASSET_LIST_PAGE_SIZE
TERMINAL_SESSION_KEEP_DURATION = CONFIG.TERMINAL_SESSION_KEEP_DURATION
TERMINAL_HOST_KEY = CONFIG.TERMINAL_HOST_KEY
TERMINAL_HEADER_TITLE = CONFIG.TERMINAL_HEADER_TITLE
# TERMINAL_TELNET_REGEX = CONFIG.TERMINAL_TELNET_REGEX

# Asset user auth external backend, default AuthBook backend
BACKEND_ASSET_USER_AUTH_VAULT = False

PERM_SINGLE_ASSET_TO_UNGROUP_NODE = CONFIG.PERM_SINGLE_ASSET_TO_UNGROUP_NODE
TICKET_AUTHORIZE_DEFAULT_TIME = CONFIG.TICKET_AUTHORIZE_DEFAULT_TIME
TICKET_AUTHORIZE_DEFAULT_TIME_UNIT = CONFIG.TICKET_AUTHORIZE_DEFAULT_TIME_UNIT
PERM_EXPIRED_CHECK_PERIODIC = CONFIG.PERM_EXPIRED_CHECK_PERIODIC
FLOWER_URL = CONFIG.FLOWER_URL

# Enable internal period task
PERIOD_TASK_ENABLED = CONFIG.PERIOD_TASK_ENABLED

# only allow single machine login with the same account
USER_LOGIN_SINGLE_MACHINE_ENABLED = CONFIG.USER_LOGIN_SINGLE_MACHINE_ENABLED

# Email custom content
EMAIL_SUBJECT_PREFIX = CONFIG.EMAIL_SUBJECT_PREFIX
EMAIL_SUFFIX = CONFIG.EMAIL_SUFFIX
EMAIL_CUSTOM_USER_CREATED_SUBJECT = CONFIG.EMAIL_CUSTOM_USER_CREATED_SUBJECT
EMAIL_CUSTOM_USER_CREATED_HONORIFIC = CONFIG.EMAIL_CUSTOM_USER_CREATED_HONORIFIC
EMAIL_CUSTOM_USER_CREATED_BODY = CONFIG.EMAIL_CUSTOM_USER_CREATED_BODY
EMAIL_CUSTOM_USER_CREATED_SIGNATURE = CONFIG.EMAIL_CUSTOM_USER_CREATED_SIGNATURE

DISPLAY_PER_PAGE = CONFIG.DISPLAY_PER_PAGE
DEFAULT_EXPIRED_YEARS = 70
USER_GUIDE_URL = CONFIG.USER_GUIDE_URL
HTTP_LISTEN_PORT = CONFIG.HTTP_LISTEN_PORT
WS_LISTEN_PORT = CONFIG.WS_LISTEN_PORT
LOGIN_LOG_KEEP_DAYS = CONFIG.LOGIN_LOG_KEEP_DAYS
TASK_LOG_KEEP_DAYS = CONFIG.TASK_LOG_KEEP_DAYS
OPERATE_LOG_KEEP_DAYS = CONFIG.OPERATE_LOG_KEEP_DAYS
ACTIVITY_LOG_KEEP_DAYS = CONFIG.ACTIVITY_LOG_KEEP_DAYS
FTP_LOG_KEEP_DAYS = CONFIG.FTP_LOG_KEEP_DAYS
CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS = CONFIG.CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS

ORG_CHANGE_TO_URL = CONFIG.ORG_CHANGE_TO_URL
WINDOWS_SKIP_ALL_MANUAL_PASSWORD = CONFIG.WINDOWS_SKIP_ALL_MANUAL_PASSWORD

AUTH_EXPIRED_SECONDS = 60 * 10

CHANGE_AUTH_PLAN_SECURE_MODE_ENABLED = CONFIG.CHANGE_AUTH_PLAN_SECURE_MODE_ENABLED

DATETIME_DISPLAY_FORMAT = '%Y-%m-%d %H:%M:%S'

TICKETS_ENABLED = CONFIG.TICKETS_ENABLED
REFERER_CHECK_ENABLED = CONFIG.REFERER_CHECK_ENABLED

CONNECTION_TOKEN_ENABLED = CONFIG.CONNECTION_TOKEN_ENABLED
# Connection token
CONNECTION_TOKEN_ONETIME_EXPIRATION = CONFIG.CONNECTION_TOKEN_ONETIME_EXPIRATION
if CONNECTION_TOKEN_ONETIME_EXPIRATION < 5 * 60:
    # 最少5分钟
    CONNECTION_TOKEN_ONETIME_EXPIRATION = 5 * 60
CONNECTION_TOKEN_REUSABLE = CONFIG.CONNECTION_TOKEN_REUSABLE
CONNECTION_TOKEN_REUSABLE_EXPIRATION = CONFIG.CONNECTION_TOKEN_REUSABLE_EXPIRATION

FORGOT_PASSWORD_URL = CONFIG.FORGOT_PASSWORD_URL

# 自定义默认组织名
GLOBAL_ORG_DISPLAY_NAME = CONFIG.GLOBAL_ORG_DISPLAY_NAME
HEALTH_CHECK_TOKEN = CONFIG.HEALTH_CHECK_TOKEN

TERMINAL_RDP_ADDR = CONFIG.TERMINAL_RDP_ADDR
SECURITY_LUNA_REMEMBER_AUTH = CONFIG.SECURITY_LUNA_REMEMBER_AUTH
SECURITY_WATERMARK_ENABLED = CONFIG.SECURITY_WATERMARK_ENABLED
SECURITY_SESSION_SHARE = CONFIG.SECURITY_SESSION_SHARE

LOGIN_REDIRECT_TO_BACKEND = CONFIG.LOGIN_REDIRECT_TO_BACKEND
LOGIN_REDIRECT_MSG_ENABLED = CONFIG.LOGIN_REDIRECT_MSG_ENABLED

TERMINAL_RAZOR_ENABLED = CONFIG.TERMINAL_RAZOR_ENABLED
TERMINAL_OMNIDB_ENABLED = CONFIG.TERMINAL_OMNIDB_ENABLED
TERMINAL_MAGNUS_ENABLED = CONFIG.TERMINAL_MAGNUS_ENABLED
TERMINAL_KOKO_SSH_ENABLED = CONFIG.TERMINAL_KOKO_SSH_ENABLED

# SMS enabled
SMS_ENABLED = CONFIG.SMS_ENABLED
SMS_BACKEND = CONFIG.SMS_BACKEND
SMS_TEST_PHONE = CONFIG.SMS_TEST_PHONE

# Alibaba
ALIBABA_ACCESS_KEY_ID = CONFIG.ALIBABA_ACCESS_KEY_ID
ALIBABA_ACCESS_KEY_SECRET = CONFIG.ALIBABA_ACCESS_KEY_SECRET
ALIBABA_VERIFY_SIGN_NAME = CONFIG.ALIBABA_VERIFY_SIGN_NAME
ALIBABA_VERIFY_TEMPLATE_CODE = CONFIG.ALIBABA_VERIFY_TEMPLATE_CODE
ALIBABA_SMS_SIGN_AND_TEMPLATES = CONFIG.ALIBABA_SMS_SIGN_AND_TEMPLATES

# TENCENT
TENCENT_SECRET_ID = CONFIG.TENCENT_SECRET_ID
TENCENT_SECRET_KEY = CONFIG.TENCENT_SECRET_KEY
TENCENT_SDKAPPID = CONFIG.TENCENT_SDKAPPID
TENCENT_VERIFY_SIGN_NAME = CONFIG.TENCENT_VERIFY_SIGN_NAME
TENCENT_VERIFY_TEMPLATE_CODE = CONFIG.TENCENT_VERIFY_TEMPLATE_CODE
TENCENT_SMS_SIGN_AND_TEMPLATES = CONFIG.TENCENT_SMS_SIGN_AND_TEMPLATES

# 公告
ANNOUNCEMENT_ENABLED = CONFIG.ANNOUNCEMENT_ENABLED
ANNOUNCEMENT = CONFIG.ANNOUNCEMENT

# help
HELP_DOCUMENT_URL = CONFIG.HELP_DOCUMENT_URL
HELP_SUPPORT_URL = CONFIG.HELP_SUPPORT_URL

SESSION_RSA_PRIVATE_KEY_NAME = 'jms_private_key'
SESSION_RSA_PUBLIC_KEY_NAME = 'jms_public_key'

OPERATE_LOG_ELASTICSEARCH_CONFIG = CONFIG.OPERATE_LOG_ELASTICSEARCH_CONFIG

MAX_LIMIT_PER_PAGE = CONFIG.MAX_LIMIT_PER_PAGE

# Magnus DB Port
MAGNUS_ORACLE_PORTS = CONFIG.MAGNUS_ORACLE_PORTS
LIMIT_SUPER_PRIV = CONFIG.LIMIT_SUPER_PRIV

LOG_NAMES = [
    'LOGIN_LOG_KEEP_DAYS', 'TASK_LOG_KEEP_DAYS',
    'OPERATE_LOG_KEEP_DAYS', 'FTP_LOG_KEEP_DAYS',
    'CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS',
    'ACTIVITY_LOG_KEEP_DAYS', 'TERMINAL_SESSION_KEEP_DURATION'
]
if LIMIT_SUPER_PRIV:
    for name in LOG_NAMES:
        if globals()[name] < 180:
            globals()[name] = 180
