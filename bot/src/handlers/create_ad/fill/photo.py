from deps import dp, Message, reply

from api import texts
from assets import CreateAdStates
from core import crop_photo
from lib import AdProxy, ask_pin_option

STATE = CreateAdStates.PHOTO


@dp.DOCUMENT.state(STATE)
def _(msg: Message):
    return reply(msg, texts.PHOTO_FILE_ERROR)


@dp.PHOTO.state(STATE)
async def _(msg: Message):
    await reply(msg, texts.PROCESS_PHOTO)
    photo = await crop_photo(msg)
    async with AdProxy.extra_info() as extra_info:
        extra_info.photo = photo
    await ask_pin_option(msg)
