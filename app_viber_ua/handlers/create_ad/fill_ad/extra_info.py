import time

from aioviber2 import types
from aioviber2.dispatcher import FSMContext
from aioviber2.types import ContentType

from models.storage import CreateAdKeys
from .... import api
from .... import config
from .... import keyboards as kb
from .... import texts
from ....conversations.fill_ad import FillAd as FillAdConv
from ....loader import dp
from ....utils import misc as funcs
from ....utils.photo_uploader import TelegraphImage
from ....utils.storage_proxies import AdProxy

Conv = FillAdConv.fill_extra_info
send_next_or_ad_preview_message = api.make_next_or_ad_preview_message_func(Conv.next)


@dp.message_handler(state=Conv.additional_info)
async def process_additional_info(message: types.Message):
    if len(message.text) > 150:
        return await message.answer(texts.too_long_answer.format(max_len=150))

    additional_info = '' if message.text == kb.Miss.MISS else message.text

    async with AdProxy.extra_info() as extra_info:
        extra_info.additional_info = additional_info

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_contact_phone, reply_markup=kb.send_contact),
    )


@dp.message_handler(state=Conv.contact_phone, content_types=[ContentType.TEXT, ContentType.CONTACT])
async def process_contact(message: types.Message):
    contact_phone = message.contact.phone_number if message.contact else message.text
    contact_phone = funcs.parse_phone_number(contact_phone)

    if contact_phone is None:
        return await message.reply(texts.enter_phone_in_right_format)

    async with AdProxy.extra_info() as extra_info:
        extra_info.contact_phone = contact_phone

    await send_next_or_ad_preview_message(
        message.answer(texts.send_photo),
    )


@dp.message_handler(content_types=ContentType.FILE, state=Conv.photo)
async def reject_photo(message: types.Message):
    await message.reply(texts.send_photo_not_file)


@dp.message_handler(content_types=ContentType.PICTURE, state=Conv.photo)
async def process_photo(message: types.Message):
    photo_url = message.media
    new_photo = TelegraphImage(dp.bot.session, photo_url, config.AD_PHOTO_RATIO)

    try:
        new_photo_url = await new_photo.get_new_image_url()
    except ValueError:
        return await message.reply(texts.photo_to_narrow)

    async with AdProxy.extra_info() as extra_info:
        extra_info.photo = new_photo_url

    text = texts.whether_pin_ad
    pin_until = await api.check_pinning_availability()

    if pin_until > time.time():  # add note about delaying
        text += '\n' + texts.pinning_will_be_delayed_until.format(
            date=funcs.repr_timestamp_as_date(pin_until)
        )

    await send_next_or_ad_preview_message(
        message.answer(text, reply_markup=kb.WhetherPin()),
    )


@dp.message_handler(button=kb.WhetherPin.PIN, state=Conv.whether_pin)
async def process_pinning(message: types.Message):
    async with AdProxy.extra_info() as extra_info:
        extra_info.pin = True

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_post_date, reply_markup=kb.Miss()),
    )


@dp.message_handler(button=kb.WhetherPin.NOT_PIN, state=Conv.whether_pin)
async def process_pinning(message: types.Message):
    async with AdProxy.extra_info() as extra_info:
        extra_info.pin = False

    await send_next_or_ad_preview_message(
        message.answer(texts.enter_post_date, reply_markup=kb.Miss()),
    )


@dp.message_handler(state=Conv.post_date)
async def process_post_date(message: types.Message, state: FSMContext):
    if message.text == kb.Miss.MISS:
        post_date = None
    else:
        try:
            post_date = funcs.parse_post_date(message.text)
        except ValueError:
            return await message.reply(texts.enter_date_in_right_format)
        else:
            if post_date < time.time():
                return await message.reply(texts.enter_later_date)

    async with AdProxy.extra_info() as extra_info:
        extra_info.post_date = post_date

    storage_data = await state.get_data()
    vacancies_amount = storage_data[CreateAdKeys.VACANCIES_AMOUNT]

    await send_next_or_ad_preview_message(
        message.answer(texts.whether_duplicate_ad, reply_markup=kb.WhetherDuplicate(vacancies_amount)),
    )


@dp.message_handler(button=kb.WhetherDuplicate.DUPLICATE, state=Conv.whether_duplicate)
async def process_duplicating(_, state: FSMContext):
    async with AdProxy.extra_info() as extra_info:
        extra_info.duplicate = True

    await state.update_data({CreateAdKeys.EDIT_MODE: True})
    await api.send_ad_preview()


@dp.message_handler(button=kb.WhetherDuplicate.NOT_DUPLICATE, state=Conv.whether_duplicate)
async def process_duplicating(_, state: FSMContext):
    async with AdProxy.extra_info() as extra_info:
        extra_info.duplicate = False

    await state.update_data({CreateAdKeys.EDIT_MODE: True})
    await api.send_ad_preview()
