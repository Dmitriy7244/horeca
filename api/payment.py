from aiohttp.web import Request

from .config import PIN_DURATION
from .helpers import get_min_pin_date
from .merchant import merchant
from .models import Order


async def on_payment(request: Request) -> Order:
    data: dict = await request.json()
    if merchant.check_payment(data):
        order = Order.get(data["order_id"])
        if order:
            update_order(order)
            return order
    raise PaymentError(data)


def update_order(order: Order):
    order.paid = True
    post_date = order.ad.extra_info.post_date or order.date
    if order.ad.extra_info.pin:
        order.pin_from = max(get_min_pin_date(order.channel_id), post_date)
        order.pin_until = order.pin_from + PIN_DURATION
    order.save()


class PaymentError(ValueError):
    def __init__(self, data: dict):
        self.data = data

    def __str__(self):
        return f"Bad data: {self.data}"
