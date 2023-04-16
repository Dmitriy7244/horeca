import asyncio

from cloudipsp import Api, Checkout
from cloudipsp.configuration import __protocol__
from cloudipsp.helpers import is_approved

from .texts import texts
from .config import MERCHANT, PAYMENT_URL
from .loader import logger


class Merchant:
    def __init__(self):
        self.api = Api(merchant_id=MERCHANT.ID, secret_key=MERCHANT.SECRET_KEY)
        self.checkout = Checkout(api=self.api)
        self.callback_url = PAYMENT_URL

    async def get_invoice_url(self, order_id: str, price: int, bot_url: str):
        data = {
            "currency": "UAH",
            "order_desc": texts.PAYMENT_FOR_ORDER,
            "amount": price * 100,
            "order_id": order_id,
            "server_callback_url": self.callback_url,
            "response_url": bot_url,
        }
        resp = await run(lambda: self.checkout.url(data))
        return resp["checkout_url"]

    def check_payment(self, data: dict) -> bool:
        try:
            return is_approved(data, self.api.secret_key, __protocol__)
        except Exception as e:
            logger.exception(e)
        return False


def run(func):
    loop = asyncio.get_running_loop()
    return loop.run_in_executor(None, func)


merchant = Merchant()
