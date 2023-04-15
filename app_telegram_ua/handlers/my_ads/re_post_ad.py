from aiogram_tools.context import callback_query as cquery, user, message, storage

from ... import api
from ... import keyboards as kb
from ...loader import dp
from ...utils.repr import repr_ad
from models.ad import Order
from models.storage import CreateAdKeys
from ...utils.storage_proxies import AdProxy
from ...conversations import FillAd
from ... import api


@dp.callback_query_handler(button=kb.MyAdsMenu.RE_POST_AD)
async def send_my_ads_menu(_, button: dict):
    order: Order = Order.objects(id=button['order_id']).first()
    await AdProxy().set_ad(order.ad)
    await storage.update_data({CreateAdKeys.EDIT_MODE: True})
    await api.send_ad_preview()
