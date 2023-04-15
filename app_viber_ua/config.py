from config import *
from utils.misc import parse_cities
from . import texts

BOT_NAME = 'Horeca Job'

BOT_TOKEN = os.getenv('VIBER_UA_BOT_TOKEN')
BOT_URI = 'viber.ua'
WEBHOOK_PATH = '/viber/ua'
PAIR_BOT_URL = 'viber://pa?chatURI=horecajobs'
FSM_DB_NAME = 'horeca_viber_ua_fsm'

CITIES = parse_cities(texts.cities)

CITIES_CHANNELS = {
    'Одеса': -1001398658451,
    'Київ': -1001238735651,
    'Харків': -1001238735651,
    'Дніпр': -1001224243674,
    'Львів': -1001269187643,
}
