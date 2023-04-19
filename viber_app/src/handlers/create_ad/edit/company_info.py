from viber import types

from .... import api0
from .... import kbs as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp
from src.utils import AdProxy

Conv = FillAd.fill_company_info


@dp.message_handler(button=kb.ChangeCompanyInfo.CITY, state=FillAd.preview_post)
async def ask_new_city(message: types.Message):
    async with AdProxy.company_info() as company_info:
        regional_city = company_info.regional_city
    await FillAd.fill_company_info.city.set()
    await message.answer(texts.choose_city, reply_markup=kb.Cities(regional_city))


@dp.message_handler(state=FillAd.preview_post)
async def ask_new_company_info(_):
    questions = {
        kb.ChangeCompanyInfo.TYPE:
            api0.Question(
                Conv.type,
                texts.enter_company_type,
            ),

        kb.ChangeCompanyInfo.NAME:
            api0.Question(
                Conv.name,
                texts.enter_company_name,
            ),

        kb.ChangeCompanyInfo.ADDRESS:
            api0.Question(
                Conv.address,
                texts.enter_company_address,
            ),
    }

    await api0.ask_for_text_or_skip(questions)
