from viber.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import texts


class Miss(ReplyKeyboardMarkup):
    MISS = texts.miss

    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(self.MISS)


class LinkButton(InlineKeyboardMarkup):
    def __init__(self, text, url):
        super().__init__()
        self.add(InlineKeyboardButton(text, url=url))
