from __future__ import annotations
import inspect
from dataclasses import dataclass
from typing import Coroutine, Callable, Union

from aioviber2 import Dispatcher, types
from aioviber2.dispatcher.handler import SkipHandler
from aioviber2.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

import api
from models.ad import Ad
from models.storage import CreateAdKeys
from .. import config
from .. import keyboards as kb
from .. import texts
from ..conversations.fill_ad import FillAd as FillAdConv, State
from ..utils.repr import repr_ad
from ..utils.storage_proxies import AdProxy

PlainAsyncFunc = Callable[[], Coroutine]
DefaultNextState = Union[State, PlainAsyncFunc]


async def send_ad_preview():
    async with AdProxy() as ad:
        vacancies_num = len(ad.vacancies)
        await types.Message.get_current().answer_picture(ad.extra_info.photo, repr_ad(ad))

    await FillAdConv.preview_post.set()
    await types.Message.get_current().answer(texts.do_you_wanna_change_ad, reply_markup=kb.ChangeAd(vacancies_num))


def make_next_or_ad_preview_message_func(default_next_state: DefaultNextState):
    async def send_next_or_ad_preview_message(next_message: Coroutine, next_state=default_next_state):
        """
        Send next_message and set next_state, but send ad preview if user in EDIT_MODE.
        Set False to next_state if you don't wanna change it.
        """
        storage_data = await Dispatcher.get_current().current_state().get_data()

        if storage_data.get(CreateAdKeys.EDIT_MODE):
            await send_ad_preview()
            next_message.close()
            return False

        if next_state is False:
            await next_message
        elif inspect.iscoroutinefunction(next_state):
            await next_message
            await next_state()
        elif isinstance(next_state, State):
            await next_message
            await next_state.set()
        else:
            raise ValueError('Wrong next state.')

        return True

    return send_next_or_ad_preview_message


async def get_channel_id_for_ad(ad: Ad = None):
    """Get channel_id for ad. Current ad is default."""
    ad = ad or await AdProxy().ad
    return config.CITIES_CHANNELS[ad.company_info.regional_city]


async def check_pinning_availability(channel_id: int = None):
    """
    Return date until-pinning-place-is-taken or 0.
    Default pinning-place is channel for current ad.
    """
    channel_id = channel_id or await get_channel_id_for_ad()
    return api.check_pinning_availability(channel_id)


# === new ===
ReplyMarkup = Union[ReplyKeyboardMarkup, InlineKeyboardMarkup, None]


@dataclass
class Question:
    next_state: State
    message_text: str
    reply_markup: ReplyMarkup = None


async def ask_for_text_or_skip(questions: dict[str, Question]):
    """
    Send Question for text in current Message.
    Raise SkipHandler if no Question provided for this text.
    """
    message = types.Message.get_current()

    if message.text not in questions:
        raise SkipHandler()

    question = questions[message.text]
    await question.next_state.set()
    await message.answer(question.message_text, reply_markup=question.reply_markup)
