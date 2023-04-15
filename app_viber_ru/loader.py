import logging

from aioviber2 import Bot, Dispatcher
from aioviber2.contrib.fsm_storage.mongo import MongoStorage

# noinspection PyUnresolvedReferences
from loader import *
from . import config

log = logging.getLogger()

bot = Bot(config.BOT_TOKEN, config.BOT_NAME, parse_mode='html', min_api_version=10)
storage = MongoStorage(db_name=config.FSM_DB_NAME)
dp = Dispatcher(bot, storage=storage)
