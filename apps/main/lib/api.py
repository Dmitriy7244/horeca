from contextlib import asynccontextmanager

import api
from api import ApiError
from deps import Message, reply, CancelHandler, get_photo_url


@asynccontextmanager
async def reply_api_error(msg: Message):
    try:
        yield
    except ApiError as e:
        await reply(msg, e.text)
        raise CancelHandler


async def check_answer_len(msg: Message):
    async with reply_api_error(msg):
        api.check_answer_len(msg.text)


async def crop_photo(msg: Message) -> str:
    async with reply_api_error(msg):
        return await api.crop_photo(await get_photo_url(msg))


async def parse_post_date(msg: Message) -> int:
    async with reply_api_error(msg):
        return api.parse_post_date(msg.text)


async def parse_phone(msg: Message, text: str) -> str:
    async with reply_api_error(msg):
        return api.parse_phone(text)


async def check_for_digits(msg: Message):
    async with reply_api_error(msg):
        api.check_for_digits(msg.text)
