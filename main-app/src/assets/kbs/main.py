from deps import (
    CallbackButton,
    UrlButton,
    InlineKeyboard,
    ReplyKeyboard,
    ContactRequestButton,
)

from api import (
    SUPPORT_URL,
    OUR_SITE_URL,
    PRICES,
    texts,
    config,
)

BACK_BUTTON = texts.BACK


class Main(InlineKeyboard):
    CREATE_AD = CallbackButton(texts.CREATE_AD)
    MY_ADS = CallbackButton(texts.MY_ADS)
    SUPPORT = UrlButton(texts.SUPPORT, SUPPORT_URL)
    OUR_SITE = UrlButton(texts.OUR_SITE, OUR_SITE_URL)
    OTHER_LANG_BOT = UrlButton(texts.OTHER_LANG_BOT, config.pair_bot_url)

    buttons = [CREATE_AD, MY_ADS, SUPPORT, OUR_SITE, OTHER_LANG_BOT]
    row_width = 2


class Region(ReplyKeyboard):
    buttons = list(config.regions)
    row_width = 2


class Cities(ReplyKeyboard):
    row_width = 2

    def __init__(self, region: str):
        super().__init__(*config.get_cities(region))


class VacancyAmount(ReplyKeyboard):
    BUTTON = texts.VACANCIES_PRICE
    buttons = []

    for amount, price in PRICES.VACANCIES.items():
        buttons.append(BUTTON.format(amount=amount, price=price))


class Skip(ReplyKeyboard):
    BUTTON = texts.SKIP
    buttons = [BUTTON]


class ContactRequest(ReplyKeyboard):
    BUTTON = ContactRequestButton(texts.SEND_PHONE)
    buttons = [BUTTON]


class PinOption(ReplyKeyboard):
    NO = texts.NOT_PIN
    YES = texts.PIN

    buttons = [NO, YES.format(price=PRICES.PIN_OPTION)]


class DuplicateOption(ReplyKeyboard):
    NO = texts.NOT_DUPLICATE
    YES = texts.DUPLICATE

    buttons = [NO]

    def __init__(self, vacancy_amount: int):
        price = PRICES.DUPLICATE_OPTION[vacancy_amount]
        button = self.YES.format(price=price)
        super().__init__(button)


class EditAd(ReplyKeyboard):
    COMPANY = texts.EDIT_COMPANY
    VACANCY = texts.EDIT_VACANCY
    OTHER_INFO = texts.EDIT_OTHER_INFO
    DONE = texts.DONE

    def __init__(self, vacancy_amount: int):
        vacancies = [self.VACANCY.format(num=i + 1) for i in range(vacancy_amount)]
        super().__init__(self.COMPANY, *vacancies, self.OTHER_INFO, self.DONE)


class EditCompany(ReplyKeyboard):
    CITY = texts.CITY
    TYPE = texts.COMPANY_TYPE
    NAME = texts.COMPANY_NAME
    ADDRESS = texts.COMPANY_ADDRESS

    buttons = [CITY, TYPE, NAME, ADDRESS, BACK_BUTTON]


class EditVacancy(ReplyKeyboard):
    TITLE = texts.VACANCY_TITLE
    WORK_EXPERIENCE = texts.WORK_EXPERIENCE
    SALARY = texts.SALARY
    SCHEDULE = texts.SCHEDULE
    WORKING_HOURS = texts.WORKING_HOURS

    buttons = [TITLE, WORK_EXPERIENCE, SALARY, SCHEDULE, WORKING_HOURS, BACK_BUTTON]


class EditOtherInfo(ReplyKeyboard):
    EXTRA_INFO = texts.EXTRA_INFO
    PHONE = texts.PHONE
    PHOTO = texts.PHOTO
    PIN_OPTION = texts.PIN_OPTION
    DUPLICATE_OPTION = texts.DUPLICATE_OPTION
    POST_DATE = texts.POST_DATE

    buttons = [
        EXTRA_INFO,
        PHONE,
        PHOTO,
        PIN_OPTION,
        DUPLICATE_OPTION,
        POST_DATE,
        BACK_BUTTON,
    ]


class Invoice(InlineKeyboard):
    CANCEL = CallbackButton(texts.CANCEL, '/start')

    def __init__(self, url: str):
        button = UrlButton(texts.PAY, url)
        super().__init__(button, self.CANCEL)


class MyAdsMenu(InlineKeyboard):
    BACK_TO_MENU = CallbackButton(texts.BACK_TO_MENU)
    REORDER = CallbackButton(texts.REORDER, "reorder:{id}")
    NEXT = CallbackButton("{}", "next-order:{index}")

    row_width = 3

    def __init__(self, order_id: str, order_index: int = 0):
        buttons = [
            self.BACK_TO_MENU,
            self.NEXT.format("➡️", index=order_index + 1),
        ]
        if order_index > 0:
            buttons = [self.NEXT.format("⬅️", index=order_index - 1), *buttons]
        super().__init__(*buttons)
        self.add(self.REORDER.format(id=order_id))
