from assets import CreateAdStates, kbs
from deps import dp, Message, FSMContext
from lib import check_edit_mode, AdProxy, ask_duplicate_option, parse_post_date


def on(button: str = None):
    return dp.text(button).state(CreateAdStates.POST_DATE)


@on(kbs.Skip.BUTTON)
def _(msg: Message, state: FSMContext):
    return callback(msg, state)


@on()
async def _(msg: Message, state: FSMContext):
    post_date = await parse_post_date(msg)
    await callback(msg, state, post_date)


async def callback(msg: Message, state: FSMContext, post_date: float = None):
    async with AdProxy.extra_info() as extra_info:
        extra_info.post_date = post_date
    await check_edit_mode(msg, state)
    await ask_duplicate_option(msg)
