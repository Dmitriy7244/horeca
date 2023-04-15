from config import *
from utils.misc import parse_cities
from . import texts

BOT_TOKEN = os.getenv('UA_BOT_TOKEN')
BOT_URI = 'telegram.ua'
WEBHOOK_PATH = '/telegram/ua'
PAIR_BOT_URL = 'https://t.me/ihorecajob_bot'
FSM_DB_NAME = 'horeca_telegram_ua_fsm'

CITIES = parse_cities(texts.cities)

CITIES_CHANNELS = {
    'Одеса': -1001398658451,
    'Київ': -1001238735651,
    'Харків': -1001238735651,
    'Дніпр': -1001224243674,
    'Львів': -1001269187643,
}
