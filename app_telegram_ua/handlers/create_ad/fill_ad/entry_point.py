from aiogram_tools.context import message

from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp

Conv = FillAd.fill_company_info


@dp.callback_query_handler(button=kb.Main.CREATE_AD)
async def start_create_vacancy(_):
    await Conv.next()
    await message.answer(texts.create_ad_guide)
    await message.answer(texts.choose_regional_city, reply_markup=kb.RegionalCities())
