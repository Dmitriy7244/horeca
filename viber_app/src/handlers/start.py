from api import texts
from viber import dp, FSMContext, SendMessageOnConversationStarted

from assets import kbs


@dp.conversation_started_handler(state="*")
async def _(_, state: FSMContext):
    await state.finish()
    return SendMessageOnConversationStarted(texts.ABOUT_US, reply_markup=kbs.MAIN)
