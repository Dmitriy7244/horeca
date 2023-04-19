from config import *
from src.utils import parse_cities
from . import texts

BOT_NAME = 'Horeca Job'

BOT_TOKEN = os.getenv('VIBER_RU_BOT_TOKEN')
BOT_URI = 'viber.ru'
WEBHOOK_PATH = '/viber/ru'
PAIR_BOT_URL = 'viber://pa?chatURI=horecajobsua'
FSM_DB_NAME = 'horeca_viber_ru_fsm'

CITIES = parse_cities(texts.cities)

CITIES_CHANNELS = {
    'Одесса': -1001398658451,
    'Киев': -1001238735651,
    'Харьков': -1001238735651,
    'Днепр': -1001224243674,
    'Львов': -1001269187643,
}
