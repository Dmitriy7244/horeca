from api import texts
from viber import StartResponse

from assets import kbs
from deps import FSMContext, dp, VIBER_MODE, reply, Message


@dp.START
async def _(msg: Message, state: FSMContext):
    await state.finish()
    if VIBER_MODE:
        return StartResponse(texts.ABOUT_US, kbs.MAIN)
    await reply(msg, texts.MENU, kbs.MAIN)
