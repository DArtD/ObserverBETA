import os

from dotenv import load_dotenv

load_dotenv()

group_chat = "-1001844038287"
BOT_TOKEN = '6008950844:AAGZx5poYNOPH1EX-M50pBUsgmmQzqqbCMg'
admin = '1982872796'
OPEN_WEATHER_TOKEN = "d7d94cd3ac0212c52fc2f6af7569d737"

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
