import os
from os import getenv


API_ID = int(getenv("API_ID", 27637482)
API_HASH = getenv("API_HASH", "176348d88118523f5b898fd15e416694)
BOT_TOKEN = getenv("BOT_TOKEN", "8131765855:AAHoBtTS6HpBLW00sDlHXhiryqIiCHwym9Y")
OWNER_ID = int(getenv("OWNER_ID", "7935947598)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "999741495  20000898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://chiruedizz:WmzSiQlS35fLDImn@cluster0.4o4zl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002335946063)
