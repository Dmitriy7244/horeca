from aiogram.utils.helper import Helper, HelperMode, Item


class CreateAdKeys(Helper):
    mode = HelperMode.snake_case

    VACANCIES_AMOUNT = Item()
    CURRENT_VACANCY_NUM = Item()
    EDIT_MODE = Item()
    CURRENT_ORDER_ID = Item()
