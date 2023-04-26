from api import texts

from assets import kbs
from deps import dp, reply, Event
from lib import ask_region


@dp.button(kbs.Main.CREATE_AD)
async def _(event: Event):
    await reply(event, texts.CREATE_AD_GUIDE)
    await ask_region(event)
