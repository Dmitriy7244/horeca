from aiogram.types import InlineKeyboardMarkup
from aiogram_tools.keyboards import InlineButton

from .. import texts


class Payment(InlineKeyboardMarkup):
    PAY = InlineButton(texts.pay, url='{payment_url}')

    def __init__(self, payment_url: str):
        super().__init__(row_width=1)
        self.add(self.PAY.format(payment_url=payment_url))
