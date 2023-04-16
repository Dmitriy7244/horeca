import time
from botty import Message, reply, ReplyKeyboard, FSMContext

from api import repr_timestamp_as_date, texts
from api.repr import repr_ad
from assets import kbs, CreateAdStates, VacancyStates, Keys
from core import ask
from .misc import check_pinning_availability
from .storage_proxies import AdProxy


def ask_region(msg: Message):
    return ask(CreateAdStates.REGION, msg, texts.ASK_REGION, kbs.REGION)


async def ask_city(msg: Message):
    async with AdProxy.company_info() as company_info:
        region = company_info.region
    await ask(CreateAdStates.CITY, msg, texts.ASK_CITY, kbs.Cities(region))


def ask_company_type(msg: Message):
    return ask(CreateAdStates.COMPANY_TYPE, msg, texts.ASK_COMPANY_TYPE, markup=False)


def ask_company_name(msg: Message):
    return ask(CreateAdStates.COMPANY_NAME, msg, texts.ASK_COMPANY_NAME)


def ask_address(msg: Message):
    return ask(CreateAdStates.ADDRESS, msg, texts.ASK_ADDRESS)


def ask_vacancy_amount(msg: Message):
    state = CreateAdStates.VACANCY_AMOUNT
    return ask(state, msg, texts.ASK_VACANCY_AMOUNT, kbs.VACANCY_AMOUNT)


async def ask_vacancy_title(msg: Message, state: FSMContext):
    session = await state.get_data()
    vacancy_num = session[Keys.VACANCY_NUM]
    await reply(msg, texts.VACANCY_NUM.format(vacancy_num))
    await ask(VacancyStates.TITLE, msg, texts.ASK_VACANCY_TITLE, markup=False)


def ask_work_experience(msg: Message):
    return ask(VacancyStates.WORK_EXPERIENCE, msg, texts.ASK_WORK_EXPERIENCE)


def ask_salary(msg: Message):
    return ask(VacancyStates.SALARY, msg, texts.ASK_SALARY)


def ask_schedule(msg: Message):
    return ask(VacancyStates.SCHEDULE, msg, texts.ASK_SCHEDULE)


def ask_working_hours(msg: Message):
    return ask(VacancyStates.WORKING_HOURS, msg, texts.ASK_WORKING_HOURS)


def ask_extra_info(msg: Message):
    return ask(CreateAdStates.EXTRA_INFO, msg, texts.ASK_EXTRA_INFO, kbs.SKIP)


def ask_phone(msg: Message):
    return ask(CreateAdStates.PHONE, msg, texts.ASK_PHONE, kbs.CONTACT_REQUEST)


def ask_photo(msg: Message):
    return ask(CreateAdStates.PHOTO, msg, texts.ASK_PHOTO, markup=False)


async def ask_pin_option(msg: Message):
    text = texts.ASK_PIN_OPTION
    pin_after = await check_pinning_availability()
    if pin_after > time.time():
        text = "\n" + texts.PIN_DELAY.format(repr_timestamp_as_date(pin_after))
    await ask(CreateAdStates.PIN_OPTION, msg, text, kbs.PIN_OPTION)


def ask_post_date(msg: Message):
    return ask(CreateAdStates.POST_DATE, msg, texts.ASK_POST_DATE, kbs.SKIP)


async def ask_duplicate_option(msg: Message, state: FSMContext):
    session = await state.get_data()
    vacancy_amount = session[Keys.VACANCY_AMOUNT]
    kb = kbs.DuplicateOption(vacancy_amount)
    await ask(CreateAdStates.DUPLICATE_OPTION, msg, texts.ASK_DUPLICATE_OPTION, kb)


async def ask_ad_edit(msg: Message):
    async with AdProxy() as ad:
        vacancy_amount = len(ad.vacancies)
    await reply(msg, repr_ad(ad))
    await ask(CreateAdStates.EDIT, msg, texts.ASK_AD_EDIT, kbs.EditAd(vacancy_amount))


def ask_item_to_edit(msg: Message, markup: ReplyKeyboard):
    return reply(msg, texts.ASK_ITEM_TO_EDIT, markup)
