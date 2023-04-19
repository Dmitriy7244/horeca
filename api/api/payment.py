from aiohttp.web import Request

from .merchant import merchant
from .models import Order


async def on_payment(request: Request) -> Order:
    data: dict = await request.json()
    if merchant.check_payment(data):
        order = Order.get_doc(data["order_id"])
        if order:
            order.paid = True
            order.save()
            return order
    raise PaymentError(data)


class PaymentError(ValueError):
    def __init__(self, data: dict):
        self.data = data

    def __str__(self):
        return f"Bad data: {self.data}"
