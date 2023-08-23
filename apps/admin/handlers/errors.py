from botty import dp


@dp.error()
async def _(upd, error):
    print(error, upd)
    return True
