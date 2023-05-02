from assets import kbs
from deps import FSMContext, dp, Message
from lib import reply_menu


@dp.button(kbs.Invoice.CANCEL).state()
async def _(msg: Message, state: FSMContext):
    await state.finish()
    await reply_menu(msg)
