from api import Order, approve_order, ADMIN_GROUP, texts
from botty import Message, reply, dp, Query, TelegramAPIError

from assets import kbs
from core import suppress


@dp.TEXT.chat_id(ADMIN_GROUP).extra(is_reply=True)
async def _edit_ad(msg: Message):
    replied_msg = msg.reply_to_message
    await reply(msg, msg.html_text, replied_msg.reply_markup)
    with suppress(TelegramAPIError):
        await msg.delete()
        await replied_msg.delete()


@dp.button(kbs.ApproveAd.BUTTON).chat_id(ADMIN_GROUP)
async def _approve_order(query: Query, button: dict):
    msg = query.message
    order = Order.get_doc(button["order_id"])
    if not order:
        return await reply(msg, texts.ORDER_NOT_FOUND)
    # await msg.edit_reply_markup(None)  # TODO
    await query.answer(texts.ORDER_PUBLISHED)
    approve_order(order)
