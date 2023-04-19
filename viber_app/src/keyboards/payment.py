from viber.types import InlineKeyboardMarkup, InlineKeyboardButton

from .. import texts


class Payment(InlineKeyboardMarkup):
    DELETE = InlineKeyboardButton(texts.delete, callback_data='/start')

    def __init__(self, payment_url: str):
        super().__init__(row_width=2)
        self.add(
            InlineKeyboardButton(texts.pay, url=payment_url),
            self.DELETE,
        )
