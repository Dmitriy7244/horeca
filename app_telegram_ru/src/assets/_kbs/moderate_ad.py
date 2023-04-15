from aiogram.types import InlineKeyboardMarkup
from aiogram_tools.keyboards import InlineButton


class ModerateAd(InlineKeyboardMarkup):
    ACCEPT = InlineButton("✅", callback="order:accept:{order_id}")

    def __init__(self, order_id: str):
        super().__init__(row_width=3, resize_keyboard=True)
        self.add(
            self.ACCEPT.format(order_id=order_id),
        )
