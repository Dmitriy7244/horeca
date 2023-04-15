from aiogram.types import ReplyKeyboardMarkup

from .. import texts

GO_BACK = texts.back_btn


class ChangeAd(ReplyKeyboardMarkup):
    COMPANY_INFO = texts.company_info
    VACANCY = texts.vacancy_num
    EXTRA_INFO = texts.extra_info
    ALL_GOOD = texts.all_good

    def __init__(self, vacancies_num: int):
        super().__init__(row_width=1, resize_keyboard=True)
        self.add(self.COMPANY_INFO)
        for i in range(1, vacancies_num + 1):
            self.add(self.VACANCY.format(vac_num=i))
        self.add(self.EXTRA_INFO, self.ALL_GOOD)


class ChangeCompanyInfo(ReplyKeyboardMarkup):
    CITY = texts.city
    TYPE = texts.type
    NAME = texts.name
    ADDRESS = texts.address

    def __init__(self):
        super().__init__(row_width=1, resize_keyboard=True)
        self.add(self.CITY, self.TYPE, self.NAME, self.ADDRESS, GO_BACK)


class ChangeVacancy(ReplyKeyboardMarkup):
    TITLE = texts.vacancy_title
    WORK_EXPERIENCE = texts.work_experience
    SALARY = texts.salary
    SCHEDULE = texts.schedule
    WORKING_HOURS = texts.working_hours

    def __init__(self):
        super().__init__(row_width=1, resize_keyboard=True)
        self.add(self.TITLE, self.WORK_EXPERIENCE, self.SALARY, self.SCHEDULE, self.WORKING_HOURS, GO_BACK)


class ChangeExtraInfo(ReplyKeyboardMarkup):
    ADDITIONAL_INFO = texts.additional_info
    CONTACT_PHONE = texts.contact_phone
    PHOTO = texts.photo
    WHETHER_PIN = texts.pinning
    WHETHER_DUPLICATE = texts.duplicating
    POST_DATE = texts.post_date

    def __init__(self):
        super().__init__(row_width=1, resize_keyboard=True)
        self.add(self.ADDITIONAL_INFO, self.CONTACT_PHONE, self.PHOTO, self.WHETHER_PIN,
                 self.WHETHER_DUPLICATE, self.POST_DATE, GO_BACK)
