from botty import Message, FSMContext, dp, reply

from api import texts
from assets import kbs


@dp.start()
async def _(msg: Message, state: FSMContext):
    await state.finish()
    await reply(msg, texts.MENU, kbs.MAIN)
