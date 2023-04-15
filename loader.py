import config
from utils.payment import Merchant
import logging

logging.basicConfig(
    level=logging.WARNING,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(config.MAIN_LOG_FILE, mode='w'),
    ]
)

merchant = Merchant(
    config.MERCHANT_ID,
    config.MERCHANT_SECRET_KEY,
    f'{config.HOST}{config.PAYMENT_PATH}'
)
