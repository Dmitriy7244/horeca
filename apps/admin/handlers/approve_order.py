from botty import reply, dp, Query

from api import Order, approve_order, ADMIN_GROUP, texts, get_webhook_url, APPROVE_ENDPOINT, send_post
from assets import kbs


@dp.button(kbs.ApproveOrder.BUTTON).chat_id(ADMIN_GROUP)
async def _(query: Query, button: dict):
    msg = query.message
    order = Order.get(button["id"])
    if not order:
        return await reply(query, texts.ORDER_NOT_FOUND)
    await query.message.edit_reply_markup()
    await query.answer(texts.ORDER_PUBLISHED)
    approve_order(order, msg.html_text)
    await notify_user(order)


def notify_user(order: Order):
    url = get_webhook_url(order) + APPROVE_ENDPOINT
    return send_post(url, params={"user_id": order.user_id})
