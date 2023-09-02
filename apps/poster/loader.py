from asyncio import run

import env
from telebot import TeleBot
from viber import bot as viber_bot

TOKEN = env.get("BOT_TOKEN")
bot = TeleBot(TOKEN, "html")
viber_bot._token = env.get("VIBER_BOT_TOKEN")
VIBER_CHAT_ID = env.get("VIBER_CHAT_ID")
