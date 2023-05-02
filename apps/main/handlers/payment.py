from aiohttp.web import Response, Request

from api import PAYMENT_ENDPOINT, texts, Order
from assets import kbs
from deps import bot, app


async def on_payment(req: Request) -> Response:
    order = Order.get(req.query["order_id"])
    await bot.send_message(order.user_id, texts.PAYMENT_SUCCESS, reply_markup=kbs.MAIN)
    return Response(body="ok")


app.router.add_post(PAYMENT_ENDPOINT, on_payment)
