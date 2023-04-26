from assets import kbs
from deps import dp, Event
from lib import reply_menu


@dp.button(kbs.MyAdsMenu.BACK_TO_MENU)
def _(event: Event):
    return reply_menu(event)
