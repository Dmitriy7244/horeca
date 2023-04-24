from viber import dp, Message, FSMContext

from assets import kbs, CreateAdStates
from lib import (
    ask_vacancy_title,
    ask_work_experience,
    ask_salary,
    ask_schedule,
    ask_working_hours,
)

Kb = kbs.EditVacancy


def on(button: str):
    return dp.text(button).state(CreateAdStates.EDIT)


@on(Kb.TITLE)
def _(msg: Message, state: FSMContext):
    return ask_vacancy_title(msg, state)


@on(Kb.WORK_EXPERIENCE)
def _(msg: Message):
    return ask_work_experience(msg)


@on(Kb.SALARY)
def _(msg: Message):
    return ask_salary(msg)


@on(Kb.SCHEDULE)
def _(msg: Message):
    return ask_schedule(msg)


@on(Kb.WORKING_HOURS)
def _(msg: Message):
    return ask_working_hours(msg)
