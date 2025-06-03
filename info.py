import re
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot Info
SESSION = environ.get('SESSION', 'TheBlackBot')
API_ID = int(environ.get('API_ID', '29450452'))
API_HASH = environ.get('API_HASH', '54759945ff88b52777eec9a455944d31')
BOT_TOKEN = environ.get('BOT_TOKEN', "7693803634:AAFIWfW8gfzMYv-G5-I9hAnge1mYFVkspio")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002101130967'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1759982322').split()]

# Bot Settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
PICS = environ.get('PICS', 'https://graph.org/file/517bc12dd5c1347df10f6.jpg').split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/b69af2db776e4e85d21ec.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/TheBlackXYZ/155")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Channels & Users
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1001889509068')) if id_pattern.search(environ.get('AUTH_CHANNEL', '')) else None
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '0')) if id_pattern.search(environ.get('REQST_CHANNEL_ID', '')) else None
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '0')) if id_pattern.search(environ.get('SUPPORT_CHAT_ID', '')) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1001860177906').split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# MongoDB
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://batman13:batman13@batman.sawvl.mongodb.net/?retryWrites=true&w=majority&appName=batman")
DATABASE_NAME = environ.get('DATABASE_NAME', "batman")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'blackcollection')

# Rename Mode
RENAME_MODE = is_enabled(environ.get('RENAME_MODE', "True"), True)

# Remove BG
RemoveBG_API = environ.get("RemoveBG_API", "")

# Links
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', '')
TUTORIAL = environ.get('TUTORIAL', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')  # No @

# Shortlink
SHORTLINK_MODE = is_enabled(environ.get('SHORTLINK_MODE', "True"), True)
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

# Clone Mode
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "True"), True)
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', '')
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '')

# Auto Approve Info
AUTO_APPROVE_MODE = is_enabled(environ.get('AUTO_APPROVE_MODE', "True"), True)
REQUEST_TO_JOIN_MODE = is_enabled(environ.get('REQUEST_TO_JOIN_MODE', "True"), True)
TRY_AGAIN_BTN = is_enabled(environ.get('TRY_AGAIN_BTN', "True"), True)

# Premium & Referral
PREMIUM_AND_REFERAL_MODE = is_enabled(environ.get('PREMIUM_AND_REFERAL_MODE', "True"), True)
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', '')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '')
OWNER_USERNAME = environ.get('OWNER_USERNAME', '')

# Stream Mode
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "True"), True)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
MULTI_CLIENT = False
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "")

# Feature Toggles
AI_SPELL_CHECK = is_enabled(environ.get('AI_SPELL_CHECK', "False"), False)
PM_SEARCH = is_enabled(environ.get('PM_SEARCH', "True"), True)
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "True"), True)
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', "True"), True)
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "False"), False)
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)

# Token Verification
VERIFY = is_enabled(environ.get('VERIFY', "False"), False)
VERIFY_SECOND_SHORTNER = is_enabled(environ.get('VERIFY_SECOND_SHORTNER', "False"), False)
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')

# Others
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', '👀 How Are You Buddy ❤️‍🩹')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "")

# ✅ Missing Template Added
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🌟 {title}</b>\n\n🎬 <b>Genre:</b> {genres}\n🗓 <b>Release:</b> {year}\n⭐ <b>Rating:</b> {rating}/10\n📖 <b>Plot:</b> {plot}")
