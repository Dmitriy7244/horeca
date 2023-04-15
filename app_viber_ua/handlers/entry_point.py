from aioviber2 import types
from aioviber2.dispatcher import FSMContext, webhook

from .. import config
from .. import keyboards as kb
from .. import texts
from ..loader import dp


@dp.conversation_started_handler()
async def send_description(_):
    return webhook.SendMessageOnConversationStarted(text=texts.description, reply_markup=kb.MenuButton())


@dp.message_handler(commands='start', state='*')
async def send_main_keyboard(msg: types.Message, state: FSMContext):
    keyboard = kb.AdminMain() if msg.from_user.id in config.ADMINS_IDS else kb.Main()
    await state.finish()
    await msg.answer(texts.main_menu, reply_markup=keyboard)


@dp.message_handler(button=kb.MyAdsMenu.MAIN_MENU, state='*')
async def send_main_keyboard(msg: types.Message, state: FSMContext):
    keyboard = kb.AdminMain() if msg.from_user.id in config.ADMINS_IDS else kb.Main()
    await state.finish()
    await msg.answer(texts.main_menu, reply_markup=keyboard)
