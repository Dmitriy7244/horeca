from api import texts
from viber import ask, Message, FSMContext, reply

from assets import kbs, CreateAdStates, Keys, VacancyStates
from .storage_proxies import AdProxy


def ask_region(msg: Message):
    return ask(CreateAdStates.REGION, msg, texts.ASK_REGION, kbs.REGION)


async def ask_city(msg: Message):
    async with AdProxy.company_info() as company_info:
        region = company_info.region
    await ask(CreateAdStates.CITY, msg, texts.ASK_CITY, kbs.Cities(region))


def ask_company_type(msg: Message):
    return ask(CreateAdStates.COMPANY_TYPE, msg, texts.ASK_COMPANY_TYPE)


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
    await ask(VacancyStates.TITLE, msg, texts.ASK_VACANCY_TITLE)
