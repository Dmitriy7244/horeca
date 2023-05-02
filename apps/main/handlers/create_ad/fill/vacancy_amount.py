from deps import dp, Message, FSMContext

from assets import kbs, CreateAdStates as States, Keys
from lib import ask_vacancy_title


@dp.text(kbs.VacancyAmount.BUTTON).state(States.VACANCY_AMOUNT)
async def _(msg: Message, state: FSMContext, button: dict):
    amount = int(button["amount"])
    session = {Keys.VACANCY_AMOUNT: amount, Keys.VACANCY_NUM: 1}
    await state.update_data(session)
    await ask_vacancy_title(msg, state)
