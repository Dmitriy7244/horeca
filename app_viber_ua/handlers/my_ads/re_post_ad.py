from aioviber2.dispatcher import FSMContext

from models.ad import Order
from models.storage import CreateAdKeys
from ... import api
from ... import keyboards as kb
from ...loader import dp
from ...utils.storage_proxies import AdProxy


@dp.message_handler(button=kb.MyAdsMenu.RE_POST_AD)
async def send_my_ads_menu(_, state: FSMContext, button: dict):
    order: Order = Order.objects(id=button['order_id']).first()
    await AdProxy().set_ad(order.ad)
    await state.update_data({CreateAdKeys.EDIT_MODE: True})
    await api.send_ad_preview()
