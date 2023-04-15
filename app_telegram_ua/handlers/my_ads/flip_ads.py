from aiogram_tools.context import callback_query as cquery, user, message

from ... import api
from ... import keyboards as kb
from ...loader import dp
from ...utils.repr import repr_ad


@dp.callback_query_handler(button=[kb.MyAdsMenu.FLIP_LEFT, kb.MyAdsMenu.FLIP_RIGHT])
async def send_my_ads_menu(_, button: dict):
    order_index = int(button['order_index'])
    order = api.orders.get_paid_order(user.id, order_index=order_index)

    if order is None:
        return await cquery.answer('Объявлений больше нет')

    await message.edit_text(repr_ad(order.ad), reply_markup=kb.MyAdsMenu(order.id, order_index=order_index))
