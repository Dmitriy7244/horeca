from botty import dp, Message, FSMContext

from assets import CreateAdStates, kbs
from core import check_answer_len
from lib import check_edit_mode, ask_phone, AdProxy


def on(button: str = None):
    return dp.text(button).state(CreateAdStates.EXTRA_INFO)


@on(kbs.Skip.BUTTON)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, "")  # TODO


@on()
def _(msg: Message, state: FSMContext):
    return callback(msg, state, msg.text)


async def callback(msg: Message, state: FSMContext, extra_info: str):
    await check_answer_len(msg)
    async with AdProxy.extra_info() as ad:
        ad.extra_info = extra_info
    await check_edit_mode(msg, state)
    await ask_phone(msg)
