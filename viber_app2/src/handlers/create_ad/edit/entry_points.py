from viber import types
from viber.dispatcher import FSMContext

from models.storage import CreateAdKeys
from .... import kbs as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp
from src.utils import AdProxy


@dp.message_handler(button=kb.GO_BACK, state=FillAd.preview_post)
async def send_change_ad_keyboard(message: types.Message):
    async with AdProxy() as ad:
        vacancies_amount = len(ad.vacancies)
    await message.answer(texts.do_you_wanna_change_ad, reply_markup=kb.ChangeAd(vacancies_amount))


@dp.message_handler(button=kb.ChangeAd.COMPANY_INFO, state=FillAd.preview_post)
async def send_change_company_info_keyboard(message: types.Message):
    await message.answer(texts.which_item_you_wanna_change, reply_markup=kb.ChangeCompanyInfo())


@dp.message_handler(button=kb.ChangeAd.VACANCY, state=FillAd.preview_post)
async def send_change_vacancy_keyboard(message: types.Message, button: dict, state: FSMContext):
    vacancy_num = int(button['vac_num'])

    async with AdProxy() as ad:
        vacancies_amount = len(ad.vacancies)

    if vacancy_num > vacancies_amount:
        return await message.answer(texts.vacancy_not_exists)

    await state.update_data({CreateAdKeys.CURRENT_VACANCY_NUM: vacancy_num})
    await message.answer(texts.which_item_you_wanna_change, reply_markup=kb.ChangeVacancy())


@dp.message_handler(button=kb.ChangeAd.EXTRA_INFO, state=FillAd.preview_post)
async def send_change_extra_info_keyboard(message: types.Message):
    await message.answer(texts.which_item_you_wanna_change, reply_markup=kb.ChangeExtraInfo())
