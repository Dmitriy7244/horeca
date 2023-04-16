import api
from aiohttp.web import Response, Request, Application
from api import PAYMENT_ENDPOINT, PaymentError
from botty import bot


async def on_payment(request: Request) -> Response:
    try:
        resp = await api.on_payment(request)
    except PaymentError as e:
        await bot.send_message(724477101, f"Payment error: {e.data}")
        return Response()
    await bot.send_message(724477101, "New payment!")
    return resp


app = Application()
app.router.add_post(PAYMENT_ENDPOINT, on_payment)
