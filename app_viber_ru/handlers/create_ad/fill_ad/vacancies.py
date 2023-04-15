import re

from aioviber2 import types
from aioviber2.dispatcher import FSMContext

from models.storage import CreateAdKeys
from .... import api
from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd as FillAdConv
from ....loader import dp
from ....utils import misc as funcs
from ....utils.storage_proxies import AdProxy

Conv = FillAdConv.fill_vacancy
send_next_or_ad_preview_message = api.make_next_or_ad_preview_message_func(Conv.next)


@dp.message_handler(button=kb.VacanciesNum.ANY_NUM, state=FillAdConv.select_vacancies_amount)
async def process_vacancies_num(message: types.Message, button: dict, state: FSMContext):
    vacancies_num = int(button['num'])
    await state.update_data({
        CreateAdKeys.VACANCIES_AMOUNT: vacancies_num,
        CreateAdKeys.CURRENT_VACANCY_NUM: 1,
    })
    await Conv.first()
    await message.answer(texts.vac_num.format(1))
    await message.answer(texts.enter_vac_title)


@dp.message_handler(state=Conv.title)
async def process_title(message: types.Message):
    title = message.text

    async with AdProxy.vacancy() as vacancy:
        vacancy.title = title

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_work_experience),
    )


@dp.message_handler(state=Conv.work_experience)
async def process_work_experience(message: types.Message):
    work_experience = funcs.uncapitalize(message.text)

    async with AdProxy.vacancy() as vacancy:
        vacancy.work_experience = work_experience

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_salary),
    )


@dp.message_handler(state=Conv.salary)
async def process_salary(message: types.Message):
    salary = funcs.uncapitalize(message.text)

    if not re.search(r'\d', salary):
        return await message.reply(texts.must_be_integer)

    async with AdProxy.vacancy() as vacancy:
        vacancy.salary = salary

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_schedule),
    )


@dp.message_handler(state=Conv.schedule)
async def process_schedule(message: types.Message):
    schedule = message.text

    if not re.search(r'\d', schedule):
        return await message.reply(texts.must_be_integer)

    async with AdProxy.vacancy() as vacancy:
        vacancy.schedule = schedule

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_working_hours),
    )


@dp.message_handler(state=Conv.working_hours)
async def process_working_hours(message: types.Message, state: FSMContext):
    storage = state

    working_hours = funcs.uncapitalize(message.text)

    if not re.search(r'\d', working_hours):
        return await message.reply(texts.must_be_integer)

    async with AdProxy.vacancy() as vacancy:
        vacancy.working_hours = working_hours

    async def ask_next_vacancy_or_extra_info():
        storage_data = await storage.get_data()
        current_vacancy_num = storage_data[CreateAdKeys.CURRENT_VACANCY_NUM]

        if current_vacancy_num < storage_data[CreateAdKeys.VACANCIES_AMOUNT]:
            await storage.update_data({CreateAdKeys.CURRENT_VACANCY_NUM: current_vacancy_num + 1})
            await Conv.first()
            await message.answer(texts.vac_num.format(current_vacancy_num + 1))
            await message.answer(texts.enter_vac_title)
        else:
            await FillAdConv.fill_extra_info.first()
            await message.answer(texts.vacancies_are_filled)
            await message.answer(texts.enter_additional_info, reply_markup=kb.Miss())

    await send_next_or_ad_preview_message(
        ask_next_vacancy_or_extra_info(),
        next_state=False,
    )
