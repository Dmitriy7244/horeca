from viber import Message

import api
from .helpers import reply_api_error


async def check_answer_len(msg: Message):
    async with reply_api_error(msg):
        api.check_answer_len(msg.text)


async def crop_photo(msg: Message) -> str:
    async with reply_api_error(msg):
        return api.crop_photo(msg.media)


async def parse_post_date(msg: Message) -> int:
    async with reply_api_error(msg):
        return api.parse_post_date(msg.text)


async def parse_phone(msg: Message, text: str) -> str:
    async with reply_api_error(msg):
        return api.parse_phone(text)


async def check_for_digits(msg: Message):
    async with reply_api_error(msg):
        api.check_for_digits(msg.text)
