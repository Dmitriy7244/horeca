from api import texts
from deps import Message, dp, reply

from assets import kbs
from lib import ask_region


@dp.button(kbs.Main.CREATE_AD)
async def _(msg: Message):
    await reply(msg, texts.CREATE_AD_GUIDE)
    await ask_region(msg)
