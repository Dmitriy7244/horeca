from .... import api0
from .... import kbs as kb
from .... import texts
from ....conversations.fill_ad import FillAd
from ....loader import dp

Conv = FillAd.fill_vacancy


@dp.message_handler(state=FillAd.preview_post)
async def ask_new_title(_):
    questions = {
        kb.ChangeVacancy.TITLE:
            api0.Question(
                Conv.title,
                texts.enter_vac_title,
            ),

        kb.ChangeVacancy.WORK_EXPERIENCE:
            api0.Question(
                Conv.work_experience,
                texts.enter_work_experience,
            ),

        kb.ChangeVacancy.SALARY:
            api0.Question(
                Conv.salary,
                texts.enter_salary,
            ),

        kb.ChangeVacancy.SCHEDULE:
            api0.Question(
                Conv.schedule,
                texts.enter_schedule,
            ),

        kb.ChangeVacancy.WORKING_HOURS:
            api0.Question(
                Conv.working_hours,
                texts.enter_working_hours,
            ),
    }

    await api0.ask_for_text_or_skip(questions)
