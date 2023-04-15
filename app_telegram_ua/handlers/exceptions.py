from ..loader import dp, log


@dp.errors_handler()
async def test(update, exc: Exception):
    log.exception(f'{exc} on {update}')
    return True
