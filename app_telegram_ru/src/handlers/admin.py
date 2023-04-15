from contextlib import suppress

import api
from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError
from aiogram_tools.context import message, callback_query as cquery
from models.ad import Order

from ... import config
from ... import kbs as kb
from ...loader import dp


@dp.message_handler(chat_id=config.ADMIN_GROUP, is_reply=True)
async def update_ad_text(_, reply: types.Message):
    await message.answer(message.html_text, reply_markup=reply.reply_markup)

    try:
        await reply.delete()
        await message.delete()
    except TelegramAPIError:
        await message.answer("Не получилось удалить изначальное сообщение")


@dp.callback_query_handler(chat_id=config.ADMIN_GROUP, button=kb.ModerateAd.ACCEPT)
async def post_ad(_, button: dict):
    order: Order = Order.objects(id=button["order_id"]).first()

    if not order:
        return await message.answer("Ошибка, заказ не найден")

    api.orders.init_order(order, message.html_text)

    await message.edit_reply_markup(None)
    await cquery.answer("Объявление опубликовано")

    with suppress(Exception):
        app = api.orders.get_app_for_order(order)
        await app.dp.bot.send_message(order.user_id, app.texts.order_approved)
