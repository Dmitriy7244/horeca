from aiogram.types import InlineKeyboardButton as InlineButton
from aiogram.types import InlineKeyboardMarkup

from .. import config
from .. import texts


class Main(InlineKeyboardMarkup):
    CREATE_AD = InlineButton(texts.create_ad_btn, callback_data=texts.create_ad_btn)
    MY_ADS = InlineButton(texts.my_ads_btn, callback_data=texts.my_ads_btn)
    TECH_SUPPORT = InlineButton(texts.tech_support_btn, url=config.TECH_SUPPORT_BOT_URL)
    OUR_SITE = InlineButton(texts.our_site_btn, url=config.HORECA_SITE_URL)
    PAIR_BOT_LINK = InlineButton(texts.another_lang_bot, url=config.PAIR_BOT_URL)

    def __init__(self):
        super().__init__(row_width=2)
        self.add(self.CREATE_AD, self.MY_ADS, self.TECH_SUPPORT, self.OUR_SITE, self.PAIR_BOT_LINK)


class AdminMain(InlineKeyboardMarkup):
    CREATE_AD = InlineButton(texts.create_ad_btn, callback_data=texts.create_ad_btn)
    MY_ADS = InlineButton(texts.my_ads_btn, callback_data=texts.my_ads_btn)
    TECH_SUPPORT = InlineButton(texts.tech_support_btn, url=config.TECH_SUPPORT_BOT_URL)
    OUR_SITE = InlineButton(texts.our_site_btn, url=config.HORECA_SITE_URL)
    PAIR_BOT_LINK = InlineButton(texts.another_lang_bot, url=config.PAIR_BOT_URL)

    GET_DUMP = InlineButton(texts.dump, callback_data=texts.dump)
    BROADCAST = InlineButton(texts.broadcast, callback_data=texts.broadcast)

    def __init__(self):
        super().__init__(row_width=2)
        self.add(self.CREATE_AD, self.MY_ADS, self.TECH_SUPPORT, self.OUR_SITE, self.PAIR_BOT_LINK)
        self.add(self.GET_DUMP, self.BROADCAST)
