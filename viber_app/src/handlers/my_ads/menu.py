from viber import dp, Message, FSMContext

import kbs
from lib import send_menu


@dp.message_handler(button=kbs.MyAdsMenu.MAIN_MENU, state='*')
def _(msg: Message, state: FSMContext):
    return send_menu(msg, state)
