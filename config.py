# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22188044"))
API_HASH = getenv("API_HASH", "099e3a1dce52b7677299c3ab8ab3b6ca")
BOT_TOKEN = getenv("BOT_TOKEN", "7782297703:AAHNSrMfuyefgGgdjxZ_hjyQteRM8s8sVKs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7080075962").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://akbarakbar4329:sFqcKBFqzsYobYfu@cluster0.keqgcg0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002341560024")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002341560024"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
