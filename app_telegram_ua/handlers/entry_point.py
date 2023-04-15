from aiogram_tools.context import message, storage, callback_query as cquery

import config
from .. import keyboards as kb
from .. import texts
from ..loader import dp


@dp.message_handler(commands='start', state='*')
async def send_main_keyboard(_):
    keyboard = kb.AdminMain() if message.from_user.id in config.ADMINS_IDS else kb.Main()
    await storage.finish()
    await message.answer(texts.main_menu, reply_markup=keyboard)


@dp.callback_query_handler(button=kb.MyAdsMenu.MAIN_MENU, state='*')
async def send_main_keyboard(_):
    keyboard = kb.AdminMain() if cquery.from_user.id in config.ADMINS_IDS else kb.Main()
    await storage.finish()
    await message.edit_text(texts.main_menu, reply_markup=keyboard)
