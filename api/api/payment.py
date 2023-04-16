from aiohttp.web import Response, Request

from .merchant import merchant
from .models import Order


async def on_payment(request: Request) -> Response:
    data: dict = await request.json()
    if merchant.check_payment(data):
        order = Order.objects(id=data["order_id"]).first()
        if order:
            order.paid_up = True
            order.save()
            return Response()
    raise PaymentError(data)


class PaymentError(ValueError):
    def __init__(self, data: dict):
        self.data = data

    def __str__(self):
        return f"Bad data: {self.data}"
