from api import get_paid_order, texts

from assets import kbs
from deps import dp, reply, Event
from lib import reply_ad


@dp.button(kbs.Main.MY_ADS)
async def _(event: Event):
    order = get_paid_order(event.from_user.id)
    if not order:
        return await reply(event, texts.NO_MY_ADS, kbs.MAIN)
    kb = kbs.MyAdsMenu(order.str_id)
    await reply_ad(event, order, kb)
