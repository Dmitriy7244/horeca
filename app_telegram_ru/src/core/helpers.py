from contextlib import asynccontextmanager

from botty import Message, reply, CancelHandler, State, ReplyKeyboard

from api import ApiError


async def ask(
    state: State,
    msg: Message,
    text: str,
    markup: ReplyKeyboard | bool = None,
):
    await state.set()
    await reply(msg, text, markup)


@asynccontextmanager
async def reply_api_error(msg: Message):
    try:
        yield
    except ApiError as e:
        await reply(msg, e.text)
        raise CancelHandler
