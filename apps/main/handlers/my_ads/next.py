from api import get_my_order, texts

from assets import kbs
from deps import dp, Event, reply
from lib import reply_ad


@dp.button(kbs.MyAdsMenu.NEXT)
async def _(event: Event, button: dict):
    index = int(button["index"])
    order = get_my_order(event.from_user.id, index)
    if order is None:
        return await reply(event, texts.NO_MORE_ADS, kbs.MAIN)
    kb = kbs.MyAdsMenu(order.str_id, index)
    await reply_ad(event, order, kb)
