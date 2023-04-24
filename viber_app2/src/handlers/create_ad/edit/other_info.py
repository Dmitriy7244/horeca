from viber import dp, Message, FSMContext

from assets import kbs, CreateAdStates
from lib import (
    ask_duplicate_option,
    ask_pin_option,
    ask_extra_info,
    ask_phone,
    ask_photo,
    ask_post_date,
)

Kb = kbs.EditOtherInfo


def on(button: str):
    return dp.text(button).state(CreateAdStates.EDIT)


@on(Kb.DUPLICATE_OPTION)
def _(msg: Message, state: FSMContext):
    return ask_duplicate_option(msg, state)


@on(Kb.PIN_OPTION)
def _(msg: Message):
    return ask_pin_option(msg)


@on(Kb.EXTRA_INFO)
def _(msg: Message):
    return ask_extra_info(msg)


@on(Kb.PHONE)
def _(msg: Message):
    return ask_phone(msg)


@on(Kb.PHOTO)
def _(msg: Message):
    return ask_photo(msg)


@on(Kb.POST_DATE)
def _(msg: Message):
    return ask_post_date(msg)
