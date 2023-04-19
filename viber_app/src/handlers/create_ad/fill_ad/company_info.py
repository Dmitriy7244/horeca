from viber import types

from .... import api
from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd as FillAdConv
from ....loader import dp
from src.utils import misc as funcs
from src.utils import AdProxy

Conv = FillAdConv.fill_company_info
send_next_or_ad_preview_message = api.make_next_or_ad_preview_message_func(Conv.next)


@dp.message_handler(button=kb.RegionalCities.BUTTONS, state=Conv.regional_city)
async def process_regional_city(msg: types.Message):
    regional_city = msg.text

    async with AdProxy.company_info() as company_info:
        company_info.regional_city = regional_city

    await send_next_or_ad_preview_message(
        msg.answer(texts.choose_city, reply_markup=kb.Cities(regional_city)),
    )


@dp.message_handler(button=kb.Cities.BUTTONS, state=Conv.city)
async def process_city(msg: types.Message):
    city = msg.text

    async with AdProxy.company_info() as company_info:
        company_info.city = city

    await send_next_or_ad_preview_message(
        msg.answer(texts.enter_company_type),
    )


@dp.message_handler(state=Conv.type)
async def process_company_type(message: types.Message):
    type = funcs.uncapitalize(message.text)

    async with AdProxy.company_info() as company_info:
        company_info.type = type

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_company_name),
    )


@dp.message_handler(state=Conv.name)
async def process_company_name(message: types.Message):
    name = message.text

    async with AdProxy.company_info() as company_info:
        company_info.name = name

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_company_address)
    )


@dp.message_handler(state=Conv.address)
async def process_company_address(message: types.Message):
    address = funcs.uncapitalize(message.text)

    async with AdProxy.company_info() as company_info:
        company_info.address = address

    await send_next_or_ad_preview_message(
        message.answer(texts.choose_vacs_num, reply_markup=kb.VacanciesNum()),
        FillAdConv.select_vacancies_amount
    )
