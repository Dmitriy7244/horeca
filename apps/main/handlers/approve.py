from aiohttp.web import Response, Request

from api import APPROVE_ENDPOINT, texts
from assets import kbs
from deps import bot, app


async def on_approve(req: Request) -> Response:
    user_id = req.query["user_id"]
    await bot.send_message(user_id, texts.ORDER_APPROVED, reply_markup=kbs.MAIN)
    return Response(body="ok")


app.router.add_post(APPROVE_ENDPOINT, on_approve)
