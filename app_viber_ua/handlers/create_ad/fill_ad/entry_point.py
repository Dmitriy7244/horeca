from aioviber2 import types

from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp

Conv = FillAd.fill_company_info


@dp.message_handler(button=kb.Main.CREATE_AD)
async def start_create_vacancy(msg: types.Message):
    await Conv.next()
    await msg.answer(texts.create_ad_guide)
    await msg.answer(texts.choose_regional_city, reply_markup=kb.RegionalCities())
