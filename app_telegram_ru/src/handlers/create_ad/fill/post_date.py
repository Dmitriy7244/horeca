from botty import dp, Message, FSMContext

from assets import CreateAdStates, kbs
from core import parse_post_date
from lib import check_edit_mode, AdProxy, ask_duplicate_option


def on(button: str = None):
    return dp.text(button, CreateAdStates.POST_DATE)


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
    await ask_duplicate_option(msg, state)
