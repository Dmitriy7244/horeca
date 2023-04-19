import api
from aiohttp.web import Response, Request, Application
from api import PAYMENT_ENDPOINT, PaymentError, ADMIN_GROUP, texts, Order, repr_ad, repr_timestamp_as_date
from botty import bot

from assets import kbs


async def on_payment(request: Request) -> Response:
    try:
        order = await api.on_payment(request)
    except PaymentError as e:
        await bot.send_message(ADMIN_GROUP, f"Payment error: {e.data}")
    else:
        await notify_user(order)
        await notify_admins(order)
    return Response()


def notify_user(order: Order):
    return bot.send_message(int(order.user_id), texts.PAYMENT_SUCCESS)


async def notify_admins(order: Order):
    kb = kbs.ApproveAd(order.id)
    ad_text = repr_ad(order.ad)
    header = texts.NEW_ORDER.format(
        user_id=order.user_id,
        order_id=order.id,
        pinning="да" if order.ad.extra_info.pin else "нет",
        duplicating="да" if order.ad.extra_info.duplicate else "нет",
        post_date=repr_timestamp_as_date(order.ad.extra_info.post_date or order.date),
    )
    await bot.send_message(ADMIN_GROUP, header)
    await bot.send_message(ADMIN_GROUP, ad_text, reply_markup=kb)


app = Application()
app.router.add_post(PAYMENT_ENDPOINT, on_payment)
