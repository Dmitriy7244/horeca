from viber import dp, Message, FSMContext

from assets import CreateAdStates
from core import parse_phone
from lib import check_edit_mode, ask_photo, AdProxy

STATE = CreateAdStates.PHONE


@dp.TEXT.state(STATE)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, msg.text)


@dp.CONTACT.state(STATE)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, msg.contact.phone_number)


async def callback(msg: Message, state: FSMContext, phone: str):
    phone = await parse_phone(msg, phone)
    async with AdProxy.extra_info() as extra_info:
        extra_info.phone = phone
    await check_edit_mode(msg, state)
    await ask_photo(msg)
