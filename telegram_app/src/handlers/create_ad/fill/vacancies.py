from botty import dp, Message, FSMContext, reply, State

from api import texts
from assets import VacancyStates as States, Keys
from core import check_for_digits
from lib import (
    AdProxy,
    ask_work_experience,
    ask_salary,
    ask_schedule,
    ask_working_hours,
    ask_vacancy_title,
    check_edit_mode,
    ask_extra_info,
)


def on(state: State):
    return dp.TEXT.state(state)


@on(States.TITLE)
async def _(msg: Message, state: FSMContext):
    async with AdProxy.vacancy() as vacancy:
        vacancy.title = msg.text
    await check_edit_mode(msg, state)
    await ask_work_experience(msg)


@on(States.WORK_EXPERIENCE)
async def _(msg: Message, state: FSMContext):
    async with AdProxy.vacancy() as vacancy:
        vacancy.work_experience = msg.text
    await check_edit_mode(msg, state)
    await ask_salary(msg)


@on(States.SALARY)
async def _(msg: Message, state: FSMContext):
    await check_for_digits(msg)
    async with AdProxy.vacancy() as vacancy:
        vacancy.salary = msg.text
    await check_edit_mode(msg, state)
    await ask_schedule(msg)


@on(States.SCHEDULE)
async def _(msg: Message, state: FSMContext):
    await check_for_digits(msg)
    async with AdProxy.vacancy() as vacancy:
        vacancy.schedule = msg.text
    await check_edit_mode(msg, state)
    await ask_working_hours(msg)


@on(States.WORKING_HOURS)
async def _(msg: Message, state: FSMContext):
    await check_for_digits(msg)
    async with AdProxy.vacancy() as vacancy:
        vacancy.working_hours = msg.text
    await check_edit_mode(msg, state)

    session = await state.get_data()
    vacancy_num = session[Keys.VACANCY_NUM]

    if vacancy_num < session[Keys.VACANCY_AMOUNT]:
        vacancy_num += 1
        await state.update_data({Keys.VACANCY_NUM: vacancy_num})
        return await ask_vacancy_title(msg, state)

    await reply(msg, texts.VACANCIES_FILLED)
    await ask_extra_info(msg)
