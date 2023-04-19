from viber import types

from ... import api0
from ... import kbs as kb
from ...loader import dp
from src.utils import repr_ad


@dp.message_handler(button=[kb.MyAdsMenu.FLIP_LEFT, kb.MyAdsMenu.FLIP_RIGHT])
async def send_my_ads_menu(msg: types.Message, button: dict):
    order_index = int(button['order_index'])
    order = api0.orders.get_paid_order(msg.from_user.id, order_index=order_index)

    if order is None:
        return await msg.answer('Объявлений больше нет', reply_markup=kb.Main())

    await msg.answer_picture(
        order.ad.extra_info.photo,
        repr_ad(order.ad),
        reply_markup=kb.MyAdsMenu(order.id, order_index=order_index)
    )
