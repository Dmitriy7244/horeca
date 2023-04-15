from botty import Query, dp, reply

from api import texts
from assets import kbs
from lib import ask_region


@dp.button(kbs.Main.CREATE_AD)
async def _(query: Query):
    await reply(query, texts.CREATE_AD_GUIDE)
    await ask_region(query.message)
