import os

from dotenv import load_dotenv

load_dotenv()

MAIN_LOG_FILE = os.getenv('MAIN_LOG_FILE')

HOST = os.getenv('HOST')
PAYMENT_PATH = '/payment'

HORECA_SITE_URL = 'https://horeca-job.com.ua/'
TECH_SUPPORT_BOT_URL = 'https://t.me/LFeedbackBot'

AD_PHOTO_RATIO = 4 / 3
MAX_VACANCIES_AMOUNT = 3
ADMIN_GROUP = -1001582277624

MAIN_DB_NAME = os.getenv('MAIN_DB_NAME')
MERCHANT_ID = int(os.getenv('MERCHANT_ID'))
MERCHANT_SECRET_KEY = os.getenv('MERCHANT_SECRET_KEY')

# (amount, price)
VACANCIES_PRICES = {1: 200, 2: 300, 3: 400}

PINNING_PRICE = 1000

# (vacancies_amount, price)
DUPLICATING_PRICES = {1: 800, 2: 1200, 3: 1600}

PINNING_TIME = 60 * 60 * 24 * 7
DUPLICATING_DELAY = 60 * 60 * 24
DUPLICATING_TIMES = 7

ADMINS_IDS = [724477101]

SSL_CERT_FILE = os.getenv('SSL_CERT_FILE')
SSL_KEY_FILE = os.getenv('SSL_KEY_FILE')
