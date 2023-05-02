from aiohttp.web import Response, Request
from botty import app, bot

import api
from api import (
    get_webhook_url,
    PAYMENT_ENDPOINT,
    Order,
    repr_ad,
    ADMIN_GROUP,
    send_post,
    make_ad_header
)
from assets import kbs


async def on_payment(req: Request) -> Response:
    order = await api.on_payment(req)
    url = get_webhook_url(order) + PAYMENT_ENDPOINT
    await notify_admins(order)
    await send_post(url, {"order_id": order.str_id})
    return Response(body="ok")


async def notify_admins(order: Order):
    kb = kbs.ApproveOrder(order.str_id)
    await bot.send_message(ADMIN_GROUP, make_ad_header(order))
    await bot.send_message(ADMIN_GROUP, repr_ad(order.ad), reply_markup=kb)

app.router.add_post("/payment", on_payment)
