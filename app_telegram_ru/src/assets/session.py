from botty import State, StatesGroup


class VacancyStates(StatesGroup):
    TITLE = State()
    WORK_EXPERIENCE = State()
    SALARY = State()
    SCHEDULE = State()
    WORKING_HOURS = State()


class CreateAdStates(StatesGroup):
    REGION = State()
    CITY = State()
    COMPANY_TYPE = State()
    COMPANY_NAME = State()
    ADDRESS = State()
    VACANCY_AMOUNT = State()
    VACANCY = VacancyStates()
    WORK_EXPERIENCE = State()
    SALARY = State()
    SCHEDULE = State()
    WORKING_HOURS = State()
    EXTRA_INFO = State()
    PHONE = State()
    PHOTO = State()
    PIN_OPTION = State()
    POST_DATE = State()
    DUPLICATE_OPTION = State()
    EDIT = State()


class Keys:
    EDIT_MODE = "edit_mode"
    VACANCY_AMOUNT = "vacancy_amount"
    VACANCY_NUM = "vacancy_num"
