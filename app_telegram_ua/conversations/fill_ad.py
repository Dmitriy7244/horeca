from aiogram.dispatcher.filters.state import State, StatesGroup


class FillCompanyInfo(StatesGroup):
    regional_city = State()
    city = State()
    type = State()
    name = State()
    address = State()


class FillVacancy(StatesGroup):
    title = State()
    work_experience = State()
    salary = State()
    schedule = State()
    working_hours = State()


class FillExtraInfo(StatesGroup):
    additional_info = State()
    contact_phone = State()
    photo = State()
    whether_pin = State()
    post_date = State()
    whether_duplicate = State()


class FillAd(StatesGroup):
    fill_company_info = FillCompanyInfo()
    select_vacancies_amount = State()
    fill_vacancy = FillVacancy()
    fill_extra_info = FillExtraInfo()
    preview_post = State()
