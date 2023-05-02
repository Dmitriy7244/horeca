from assets import CreateAdStates, kbs
from deps import dp, Message, FSMContext
from lib import check_edit_mode, ask_phone, AdProxy, check_answer_len


def on(button: str = None):
    return dp.text(button).state(CreateAdStates.EXTRA_INFO)


@on(kbs.Skip.BUTTON)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, "")


@on()
def _(msg: Message, state: FSMContext):
    return callback(msg, state, msg.text)


async def callback(msg: Message, state: FSMContext, extra_info: str):
    await check_answer_len(msg)
    async with AdProxy.extra_info() as ad:
        ad.extra_info = extra_info
    await check_edit_mode(msg, state)
    await ask_phone(msg)
