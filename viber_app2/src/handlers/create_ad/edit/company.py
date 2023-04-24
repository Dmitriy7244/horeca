from viber import dp, Message

from assets import kbs, CreateAdStates
from lib import ask_company_type, ask_company_name, ask_address, ask_city

Kb = kbs.EditCompany


def on(button: str):
    return dp.text(button).state(CreateAdStates.EDIT)


@on(Kb.CITY)
def _(msg: Message):
    return ask_city(msg)


@on(Kb.TYPE)
def _(msg: Message):
    return ask_company_type(msg)


@on(Kb.NAME)
def _(msg: Message):
    return ask_company_name(msg)


@on(Kb.ADDRESS)
def _(msg: Message):
    return ask_address(msg)
