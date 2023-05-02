from assets import CreateAdStates
from deps import dp, Message, FSMContext
from lib import check_edit_mode, ask_photo, AdProxy, parse_phone

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
