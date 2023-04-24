from viber import Message, CancelHandler, FSMContext

from assets import Keys
from .questions import ask_ad_edit


async def check_edit_mode(msg: Message, state: FSMContext):
    session = await state.get_data()
    if not session.get(Keys.EDIT_MODE):
        return
    await ask_ad_edit(msg)
    raise CancelHandler
