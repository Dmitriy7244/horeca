from contextlib import suppress

from aiogram.utils.exceptions import TelegramAPIError
from aiohttp import web

import api
import app_telegram_ru
import app_telegram_ua
import config
from loader import merchant
from models.ad import Order

from api.models import Order


async def notify_user_on_payment(order: Order):
    app = api.orders.get_app_for_order(order)

    with suppress(TelegramAPIError):
        await app.dp.bot.send_message(order.user_id, app.texts.succeeded_payment)


async def notify_admins_on_payment(order: Order):
    app = app_telegram_ru
    dp = app.dp
    kb = app.keyboards

    if 'ru' in order.created_from:
        ad_text = app_telegram_ru.utils.repr.repr_ad(order.ad)
    else:
        ad_text = app_telegram_ua.utils.repr.repr_ad(order.ad)

    header = app.texts.order_info.format(
        user_id=order.user_id,
        order_id=order.id,
        pinning='да' if order.ad.extra_info.pin else 'нет',
        duplicating='да' if order.ad.extra_info.duplicate else 'нет',
        post_date=api.get_date_from_timestamp(order.ad.extra_info.post_date or order.date),
    )

    with suppress(TelegramAPIError):
        await dp.bot.send_message(config.ADMIN_GROUP, header)
        await dp.bot.send_message(config.ADMIN_GROUP, ad_text, reply_markup=kb.ModerateAd(order.id))


async def process_payment(request: web.Request):
    data: dict = await request.json()

    if merchant.check_payment(data):
        order = Order.objects(id=data['order_id']).first()
        if order:
            order.paid_up = True
            order.save()

            await notify_user_on_payment(order)
            await notify_admins_on_payment(order)

    return web.Response()
