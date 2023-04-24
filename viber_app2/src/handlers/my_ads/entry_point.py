from aiogram_tools.context import callback_query as cquery, user, message

from ... import api
from ... import kbs as kb
from ...loader import dp
from ...utils.repr import repr_ad


@dp.callback_query_handler(button=kb.Main.MY_ADS)
async def send_my_ads_menu(_):
    order = api.orders.get_paid_order(user.id, order_index=0)

    if order is None:
        return await cquery.answer("У вас еще нет объявлений")

    await message.edit_text(
        repr_ad(order.ad), reply_markup=kb.MyAdsMenu(order.id, order_index=0)
    )
