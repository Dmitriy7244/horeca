import env
from telebot import TeleBot

TOKEN = env.get("BOT_TOKEN")
bot = TeleBot(TOKEN, "html")
