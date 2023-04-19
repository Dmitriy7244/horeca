from api import config
from viber.types import ReplyKeyboardMarkup, KeyboardButton

import texts


class Region(ReplyKeyboardMarkup):
    buttons = list(config.regions)

    def __init__(self):
        super().__init__(row_width=2, resize_keyboard=True)
        self.add(*self.buttons)


class Cities(ReplyKeyboardMarkup):
    def __init__(self, region: str):
        super().__init__(row_width=2, resize_keyboard=True)
        self.add(*config.get_cities(region))


class VacancyAmount(ReplyKeyboardMarkup):
    ANY_NUM = texts.vacancies_num_and_prices

    def __init__(self):
        super().__init__(row_width=1, resize_keyboard=True)
        for num, price in config.VACANCIES_PRICES.items():
            vac_word = get_word_form(num, *texts.vac_word_forms.split(';'))
            self.add(self.ANY_NUM.format(num=num, vac_word=vac_word, price=price))


class WhetherPin(ReplyKeyboardMarkup):
    NOT_PIN = texts.not_pin
    PIN = texts.pin_for

    def __init__(self):
        super().__init__(row_width=1, resize_keyboard=True)
        self.add(
            self.NOT_PIN,
            self.PIN.format(price=config.PINNING_PRICE),
        )


class WhetherDuplicate(ReplyKeyboardMarkup):
    NOT_DUPLICATE = texts.not_duplicate
    DUPLICATE = texts.duplicate

    def __init__(self, vacancies_num: int):
        super().__init__(row_width=1, resize_keyboard=True)
        self.add(self.NOT_DUPLICATE)
        self.add(self.DUPLICATE.format(price=config.DUPLICATING_PRICES[vacancies_num]))


send_contact = ReplyKeyboardMarkup(resize_keyboard=True)
send_contact.add(KeyboardButton(texts.send_phone_number, request_contact=True))
