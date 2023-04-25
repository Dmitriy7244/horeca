from contextlib import asynccontextmanager

from api import ApiError
from deps import Message, reply, CancelHandler


@asynccontextmanager
async def reply_api_error(msg: Message):
    try:
        yield
    except ApiError as e:
        await reply(msg, e.text)
        raise CancelHandler
