import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram_tools import Dispatcher

from . import config

log = logging.getLogger()

bot = Bot(config.BOT_TOKEN, parse_mode='html')
storage = MongoStorage(db_name=config.FSM_DB_NAME)
dp = Dispatcher(bot, storage=storage)
