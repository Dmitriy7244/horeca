from aiogram.types import InlineKeyboardMarkup
from aiogram_tools.keyboards import InlineButton


class MyAdsMenu(InlineKeyboardMarkup):
    MAIN_MENU = InlineButton("Меню", callback="Меню")
    RE_POST_AD = InlineButton(
        "Разместить повторно", callback="Разместить повторно:{order_id}"
    )
    FLIP_LEFT = InlineButton("<", callback="get:paid_order:{order_index}")
    FLIP_RIGHT = InlineButton(">", callback="get:paid_order:{order_index}")

    def __init__(self, order_id: str, order_index: int):
        super().__init__(resize_keyboard=True)
        self.row(
            self.FLIP_LEFT.format(order_index=order_index - 1),
            self.MAIN_MENU,
            self.FLIP_RIGHT.format(order_index=order_index + 1),
        )

        self.row(self.RE_POST_AD.format(order_id=order_id))
