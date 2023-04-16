from botty import dp, Message, FSMContext

from assets import CreateAdStates, kbs
from lib import check_edit_mode, ask_post_date, AdProxy


def on(button: str):
    return dp.text(button, CreateAdStates.PIN_OPTION)


@on(kbs.PinOption.YES)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, option=True)


@on(kbs.PinOption.NO)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, option=False)


async def callback(msg: Message, state: FSMContext, option: bool):
    async with AdProxy.extra_info() as extra_info:
        extra_info.pin = option
    await check_edit_mode(msg, state)
    await ask_post_date(msg)
