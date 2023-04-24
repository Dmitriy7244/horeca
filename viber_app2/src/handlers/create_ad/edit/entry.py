from viber import dp, Message, FSMContext, reply

from api import texts
from assets import kbs, Keys, CreateAdStates
from lib import AdProxy, ask_ad_edit, ask_item_to_edit

Kb = kbs.EditAd


def on(button: str):
    return dp.text(button).state(CreateAdStates.EDIT)


@on(kbs.BACK_BUTTON)
def _(msg: Message):
    return ask_ad_edit(msg)


@on(Kb.COMPANY)
def _(msg: Message):
    return ask_item_to_edit(msg, kbs.EDIT_COMPANY)


@on(Kb.VACANCY)
async def _(msg: Message, state: FSMContext, button: dict):
    vacancy_num = int(button["num"])
    async with AdProxy() as ad:
        vacancies_amount = len(ad.vacancies)
    if vacancy_num > vacancies_amount:
        return await reply(msg, texts.vacancy_not_exists)
    await state.update_data({Keys.VACANCY_NUM: vacancy_num})
    await ask_item_to_edit(msg, kbs.EDIT_VACANCY)


@on(Kb.OTHER_INFO)
def _(msg: Message):
    return ask_item_to_edit(msg, kbs.EDIT_OTHER_INFO)
