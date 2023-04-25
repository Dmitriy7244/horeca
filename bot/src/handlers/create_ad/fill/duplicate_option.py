from deps import dp, Message, FSMContext

from assets import CreateAdStates, kbs, Keys
from lib import AdProxy, ask_ad_edit, set_edit_mode


def on(button: str):
    return dp.text(button).state(CreateAdStates.DUPLICATE_OPTION)


@on(kbs.DuplicateOption.YES)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, option=True)


@on(kbs.DuplicateOption.NO)
def _(msg: Message, state: FSMContext):
    return callback(msg, state, option=False)


async def callback(msg: Message, state: FSMContext, option: bool):
    async with AdProxy.extra_info() as extra_info:
        extra_info.duplicate = option
    await set_edit_mode(state)
    await ask_ad_edit(msg)
