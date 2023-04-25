from loader import dp


@dp.callback_query_handler(button=kb.MyAdsMenu.MAIN_MENU, state="*")  # TODO
async def send_main_keyboard(_):
    keyboard = kb.AdminMain() if cquery.from_user.id in config.ADMINS_IDS else kb.Main()
    await storage.finish()
    await message.edit_text(texts.main_menu, reply_markup=keyboard)
