from .... import api
from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp

Conv = FillAd.fill_vacancy


@dp.message_handler(state=FillAd.preview_post)
async def ask_new_title(_):
    questions = {
        kb.ChangeVacancy.TITLE:
            api.Question(
                Conv.title,
                texts.enter_vac_title,
            ),

        kb.ChangeVacancy.WORK_EXPERIENCE:
            api.Question(
                Conv.work_experience,
                texts.enter_work_experience,
            ),

        kb.ChangeVacancy.SALARY:
            api.Question(
                Conv.salary,
                texts.enter_salary,
            ),

        kb.ChangeVacancy.SCHEDULE:
            api.Question(
                Conv.schedule,
                texts.enter_schedule,
            ),

        kb.ChangeVacancy.WORKING_HOURS:
            api.Question(
                Conv.working_hours,
                texts.enter_working_hours,
            ),
    }

    await api.ask_for_text_or_skip(questions)
