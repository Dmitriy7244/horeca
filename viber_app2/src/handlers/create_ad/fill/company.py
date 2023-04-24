from viber import dp, Message, FSMContext, State

from assets import kbs, CreateAdStates as States
from lib import (
    AdProxy,
    ask_city,
    ask_address,
    ask_company_name,
    ask_company_type,
    ask_vacancy_amount,
    check_edit_mode,
)


def on(state: State, button: str = None):
    return dp.text(button).state(state)


@on(States.REGION, kbs.Region.buttons)
async def _(msg: Message, state: FSMContext):
    async with AdProxy.company_info() as company_info:
        company_info.region = msg.text  # TODO
    await check_edit_mode(msg, state)
    await ask_city(msg)


@on(States.CITY)  # TODO: check cities
async def _(msg: Message, state: FSMContext):
    async with AdProxy.company_info() as company_info:
        company_info.city = msg.text
    await check_edit_mode(msg, state)
    await ask_company_type(msg)


@on(States.COMPANY_TYPE)
async def _(msg: Message, state: FSMContext):
    async with AdProxy.company_info() as company_info:
        company_info.type = msg.text
    await check_edit_mode(msg, state)
    await ask_company_name(msg)


@on(States.COMPANY_NAME)
async def _(msg: Message, state: FSMContext):
    async with AdProxy.company_info() as company_info:
        company_info.name = msg.text
    await check_edit_mode(msg, state)
    await ask_address(msg)


@on(States.ADDRESS)
async def _(msg: Message, state: FSMContext):
    async with AdProxy.company_info() as company_info:
        company_info.address = msg.text
    await check_edit_mode(msg, state)
    await ask_vacancy_amount(msg)
