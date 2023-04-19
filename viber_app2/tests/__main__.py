from viber import dp, Message, run, reply
from api import texts
from lib import ask_company_type


@dp.message_handler(state="*")
def _(msg: Message):
    return reply(msg, texts.PIN_DELAY)


run()
