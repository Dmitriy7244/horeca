import api
from api import config, texts, Order, repr_ad

from assets import kbs, Keys
from deps import reply, VIBER_MODE, InlineKeyboard, Event, FSMContext
from .storage_proxies import AdProxy


async def get_ad_channel() -> int:
    ad = await AdProxy().ad
    return config.get_channel(ad.company_info.region)


async def get_min_pin_date() -> int:
    channel_id = await get_ad_channel()
    return api.get_min_pin_date(channel_id)


def reply_menu(event: Event):
    return reply(event, texts.MENU, kbs.MAIN)


def reply_ad(event: Event, order: Order, kb: InlineKeyboard):
    if VIBER_MODE:
        text = repr_ad(order.ad, with_photo=False)
        return event.answer_photo(order.ad.extra_info.photo, text, reply_markup=kb)
    else:
        return reply(event, repr_ad(order.ad), kb)


def set_edit_mode(state: FSMContext):
    return state.update_data({Keys.EDIT_MODE: True})
