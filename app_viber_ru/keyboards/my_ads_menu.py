from aioviber2.types import InlineKeyboardMarkup, InlineKeyboardButton


class MyAdsMenu(InlineKeyboardMarkup):
    MAIN_MENU = InlineKeyboardButton('Меню', callback_data='Меню')
    RE_POST_AD = InlineKeyboardButton('Разместить повторно', callback_data='Разместить повторно:{order_id}')
    FLIP_LEFT = InlineKeyboardButton('⬅️', callback_data='get:paid_order:{order_index}')
    FLIP_RIGHT = InlineKeyboardButton('➡️', callback_data='get:paid_order:{order_index}')

    def __init__(self, order_id: str, order_index: int):
        super().__init__(resize_keyboard=True)
        self.row(
            InlineKeyboardButton(
                self.FLIP_LEFT.text,
                callback_data=self.FLIP_LEFT.callback_data.format(order_index=order_index - 1),
            ),
            self.MAIN_MENU,
            InlineKeyboardButton(
                self.FLIP_RIGHT.text,
                callback_data=self.FLIP_RIGHT.callback_data.format(order_index=order_index + 1),
            ),
        )

        self.row(
            InlineKeyboardButton(
                self.RE_POST_AD.text,
                callback_data=self.RE_POST_AD.callback_data.format(order_id=order_id),
            ),
        )
