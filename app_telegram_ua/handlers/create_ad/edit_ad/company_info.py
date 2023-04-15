from aiogram.types import ReplyKeyboardRemove
from aiogram_tools.context import message

from .... import api
from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp
from ....utils.storage_proxies import AdProxy

Conv = FillAd.fill_company_info


@dp.message_handler(button=kb.ChangeCompanyInfo.CITY, state=FillAd.preview_post)
async def ask_new_city(_):
    async with AdProxy.company_info() as company_info:
        regional_city = company_info.regional_city
    await FillAd.fill_company_info.city.set()
    await message.answer(texts.choose_city, reply_markup=kb.Cities(regional_city))


@dp.message_handler(state=FillAd.preview_post)
async def ask_new_company_info(_):
    questions = {
        kb.ChangeCompanyInfo.TYPE:
            api.Question(
                Conv.type,
                texts.enter_company_type,
                ReplyKeyboardRemove(),
            ),

        kb.ChangeCompanyInfo.NAME:
            api.Question(
                Conv.name,
                texts.enter_company_name,
                ReplyKeyboardRemove(),
            ),

        kb.ChangeCompanyInfo.ADDRESS:
            api.Question(
                Conv.address,
                texts.enter_company_address,
                ReplyKeyboardRemove(),
            ),
    }

    await api.ask_for_text_or_skip(questions)