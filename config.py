# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24954614"))
API_HASH = getenv("API_HASH", "854d71e266722a054d214898c754c70b")
BOT_TOKEN = getenv("BOT_TOKEN", "7554255653:AAHJux31c1Q-nZLx3CAgHTqRhsgLHFTxInE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5716292248").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://jeetnarayantiwari5:FGXfMWTnAsaEB4u2@cluster0.2whtu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002486152287")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002401910672"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "70"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
