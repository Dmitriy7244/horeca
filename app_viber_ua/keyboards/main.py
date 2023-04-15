from aioviber2.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from .. import config
from .. import texts


class MenuButton(ReplyKeyboardMarkup):
    MENU = texts.menu

    def __init__(self):
        super().__init__(resize_keyboard=True)
        self.add(self.MENU)


class Main(InlineKeyboardMarkup):
    CREATE_AD = InlineKeyboardButton(texts.create_ad_btn, callback_data=texts.create_ad_btn)
    MY_ADS = InlineKeyboardButton(texts.my_ads_btn, callback_data=texts.my_ads_btn)
    TECH_SUPPORT = InlineKeyboardButton(texts.tech_support_btn, url=config.TECH_SUPPORT_BOT_URL)
    OUR_SITE = InlineKeyboardButton(texts.our_site_btn, url=config.HORECA_SITE_URL)
    PAIR_BOT_LINK = InlineKeyboardButton(texts.another_lang_bot, url=config.PAIR_BOT_URL)

    def __init__(self):
        super().__init__(row_width=2)
        self.add(self.CREATE_AD, self.MY_ADS, self.TECH_SUPPORT, self.OUR_SITE, self.PAIR_BOT_LINK)


class AdminMain(InlineKeyboardMarkup):
    CREATE_AD = InlineKeyboardButton(texts.create_ad_btn, callback_data=texts.create_ad_btn)
    MY_ADS = InlineKeyboardButton(texts.my_ads_btn, callback_data=texts.my_ads_btn)
    TECH_SUPPORT = InlineKeyboardButton(texts.tech_support_btn, url=config.TECH_SUPPORT_BOT_URL)
    OUR_SITE = InlineKeyboardButton(texts.our_site_btn, url=config.HORECA_SITE_URL)
    PAIR_BOT_LINK = InlineKeyboardButton(texts.another_lang_bot, url=config.PAIR_BOT_URL)

    GET_DUMP = InlineKeyboardButton(texts.dump, callback_data=texts.dump)
    BROADCAST = InlineKeyboardButton(texts.broadcast, callback_data=texts.broadcast)

    def __init__(self):
        super().__init__(row_width=2)
        self.add(self.CREATE_AD, self.MY_ADS, self.TECH_SUPPORT, self.OUR_SITE, self.PAIR_BOT_LINK)
        self.add(self.GET_DUMP, self.BROADCAST)
