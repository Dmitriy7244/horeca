import asyncio
from time import time

from botty import dp

from api import (
    APPROVE_ENDPOINT,
    Order,
    Post,
    get_webhook_url,
    send_post,
)


def notify_user(order: Order):
    url = get_webhook_url(order) + APPROVE_ENDPOINT
    return send_post(url, params={"user_id": order.user_id})
