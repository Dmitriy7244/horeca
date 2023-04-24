from api import texts
from viber import FSMContext, dp, StartResponse

from assets import kbs


@dp.START
async def _(_, state: FSMContext):
    await state.finish()
    return StartResponse(texts.ABOUT_US, kbs.MAIN)
