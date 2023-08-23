from contextlib import suppress

from botty import Message, TelegramAPIError, dp, reply

from api import ADMIN_GROUP


@dp.TEXT.chat_id(ADMIN_GROUP).has_reply
async def _(msg: Message):
    replied_msg = msg.reply_to_message
    await reply(msg, msg.html_text, replied_msg.reply_markup)
    with suppress(TelegramAPIError):
        await msg.delete()
        await replied_msg.delete()
