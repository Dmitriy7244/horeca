from aioviber2 import types

from ... import api
from ... import keyboards as kb
from ...loader import dp
from ...utils.repr import repr_ad


@dp.message_handler(button=kb.Main.MY_ADS)
async def send_my_ads_menu(msg: types.Message):
    order = api.orders.get_paid_order(msg.from_user.id, order_index=0)

    if order is None:
        return await msg.answer('У вас еще нет объявлений')

    await msg.answer_picture(
        order.ad.extra_info.photo,
        repr_ad(order.ad),
        reply_markup=kb.MyAdsMenu(order.id, order_index=0)
    )
