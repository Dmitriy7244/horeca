from viber import types

from ... import api0
from ... import kbs as kb
from ...loader import dp
from src.utils import repr_ad


@dp.message_handler(button=kb.Main.MY_ADS)
async def send_my_ads_menu(msg: types.Message):
    order = api0.orders.get_paid_order(msg.from_user.id, order_index=0)

    if order is None:
        return await msg.answer('У вас еще нет объявлений')

    await msg.answer_picture(
        order.ad.extra_info.photo,
        repr_ad(order.ad),
        reply_markup=kb.MyAdsMenu(order.id, order_index=0)
    )
