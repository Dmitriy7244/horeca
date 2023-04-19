from api import texts
from viber import Message, FSMContext, reply

from assets import kbs


async def send_menu(msg: Message, state: FSMContext):
    await state.finish()
    await reply(msg, texts.MENU, kbs.MAIN)
