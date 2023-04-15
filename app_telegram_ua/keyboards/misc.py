from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram_tools.keyboards import InlineButton

from .. import texts


class Miss(ReplyKeyboardMarkup):
    MISS = texts.miss

    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(self.MISS)


class LinkButton(InlineKeyboardMarkup):
    def __init__(self, text, url):
        super().__init__()
        self.add(InlineButton(text, url=url))
