import asyncio
from time import time

from botty import Query, dp, reply
from lib import notify_user, schedule_post

from api import (
    ADMIN_GROUP,
    APPROVE_ENDPOINT,
    Order,
    Post,
    approve_order,
    get_webhook_url,
    save_post,
    send_post,
    texts,
)
from assets import kbs


@dp.button(kbs.ApproveOrder.BUTTON).chat_id(ADMIN_GROUP)
async def _(query: Query, button: dict):
    msg = query.message
    order = Order.get(button["id"])
    if not order:
        return await reply(query, texts.ORDER_NOT_FOUND)
    await query.message.edit_reply_markup()
    await query.answer(texts.ORDER_PUBLISHED)
    order = approve_order(order, msg.html_text)
    save_post(order)
    await notify_user(order)
