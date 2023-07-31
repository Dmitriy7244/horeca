

from api import (
    APPROVE_ENDPOINT,
    Order,
    get_webhook_url,
    send_post,
)


def notify_user(order: Order):
    url = get_webhook_url(order) + APPROVE_ENDPOINT
    return send_post(url, params={"user_id": order.user_id})
