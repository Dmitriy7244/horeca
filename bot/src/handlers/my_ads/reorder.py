from api import Order

from assets import kbs
from deps import dp, Event, FSMContext
from lib import ask_ad_edit, AdProxy, set_edit_mode


@dp.button(kbs.MyAdsMenu.REORDER)
async def _(event: Event, button: dict, state: FSMContext):
    order = Order.get_doc(button["id"])
    await AdProxy().set_ad(order.ad)
    await set_edit_mode(state)
    await ask_ad_edit(event)
