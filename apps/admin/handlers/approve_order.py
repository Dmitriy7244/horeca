from botty import Query, dp, reply
from lib import notify_user

from api import (
    ADMIN_GROUP,
    Order,
    approve_order,
    save_post,
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
