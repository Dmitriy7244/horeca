from core import dp, Message, reply, crop_photo, parse_post_date


@dp.photo(state="*")
async def _(msg: Message):
    result = await crop_photo(msg)
    await reply(msg, str(result))


@dp.command("test", state="*")
def _(msg: Message):
    return reply(msg, "...")


@dp.text(state="*")
async def _(msg: Message):
    result = await parse_post_date(msg)
    await reply(msg, str(result))


dp.run()
