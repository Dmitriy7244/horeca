import api
from aiohttp import ClientSession
from aiohttp.web import Response, Request
from api import get_webhook_url, PAYMENT_ENDPOINT
from botty import app


async def on_payment(req: Request) -> Response:
    order = await api.on_payment(req)
    url = get_webhook_url(order) + PAYMENT_ENDPOINT
    session = ClientSession()
    async with session.post(url, params={"order_id": order.str_id}) as resp:
        resp.raise_for_status()
    return Response(body="ok")


def setup():
    app.router.add_post("/payment", on_payment)
