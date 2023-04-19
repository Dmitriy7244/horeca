from viber.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

import texts
from api import SUPPORT_URL, OUR_SITE_URL, config


class MenuButton(ReplyKeyboardMarkup):
    BUTTON = texts.menu

    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(self.BUTTON)


class Main(InlineKeyboardMarkup):
    CREATE_AD = InlineKeyboardButton(texts.create_ad_btn, callback_data=texts.create_ad_btn)
    MY_ADS = InlineKeyboardButton(texts.my_ads_btn, callback_data=texts.my_ads_btn)
    TECH_SUPPORT = InlineKeyboardButton(texts.tech_support_btn, url=SUPPORT_URL)
    OUR_SITE = InlineKeyboardButton(texts.our_site_btn, url=OUR_SITE_URL)
    PAIR_BOT_LINK = InlineKeyboardButton(texts.another_lang_bot, url=config.pair_bot_url)

    def __init__(self):
        super().__init__(row_width=2)
        self.add(self.CREATE_AD, self.MY_ADS, self.TECH_SUPPORT, self.OUR_SITE, self.PAIR_BOT_LINK)
