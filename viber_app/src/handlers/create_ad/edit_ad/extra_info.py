import time

from viber import types

from .... import api
from .... import keyboards as kb
from .... import texts
from .... import utils
from ....conversations.fill_ad import FillAd
from ....loader import dp
from ....utils.storage_proxies import AdProxy

Conv = FillAd.fill_extra_info


@dp.message_handler(button=kb.ChangeExtraInfo.WHETHER_DUPLICATE, state=FillAd.preview_post)
async def ask_new_duplicating(message: types.Message):
    async with AdProxy() as ad:
        vacancies_amount = len(ad.vacancies)
    await FillAd.fill_extra_info.whether_duplicate.set()
    await message.answer(texts.whether_duplicate_ad, reply_markup=kb.WhetherDuplicate(vacancies_amount))


@dp.message_handler(button=kb.ChangeExtraInfo.WHETHER_PIN, state=FillAd.preview_post)
async def ask_new_pinning(message: types.Message):
    text = texts.whether_pin_ad
    pin_until = await api.check_pinning_availability()

    if pin_until > time.time():  # add note about delaying
        text += '\n' + texts.pinning_will_be_delayed_until.format(
            date=utils.misc.repr_timestamp_as_date(pin_until)
        )

    await FillAd.fill_extra_info.whether_pin.set()
    await message.answer(text, reply_markup=kb.WhetherPin())


@dp.message_handler(state=FillAd.preview_post)
async def ask_new_extra_info(_):
    questions = {
        kb.ChangeExtraInfo.ADDITIONAL_INFO:
            api.Question(
                Conv.additional_info,
                texts.enter_additional_info,
                kb.Miss(),
            ),

        kb.ChangeExtraInfo.CONTACT_PHONE:
            api.Question(
                Conv.contact_phone,
                texts.enter_contact_phone,
                kb.send_contact,
            ),

        kb.ChangeExtraInfo.PHOTO:
            api.Question(
                Conv.photo,
                texts.send_photo,
            ),

        kb.ChangeExtraInfo.POST_DATE:
            api.Question(
                Conv.post_date,
                texts.enter_post_date,
                kb.Miss()
            )
    }

    await api.ask_for_text_or_skip(questions)
