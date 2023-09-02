import re
from datetime import datetime
from time import time

from aiohttp import ClientSession

from .config import (
    APP_ID,
    APP_URL,
    DUPLICATE_INTERVAL,
    DUPLICATE_TIMES,
    PIN_DURATION,
    PRICES,
)
from .lib import safe_html
from .merchant import merchant
from .models import Ad, Invoice, Order, Post, Webhook
from .repr import repr_ad
from .texts import texts


def repr_timestamp_as_date(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M")


def get_min_pin_date(channel_id: int) -> int:
    filters = {"paid": True, "channel_id": channel_id}
    until_dates = [o.pin_until for o in Order.find_all(**filters) if o.pin_until]
    return max(until_dates) if until_dates else 0


def approve_order(order: Order, final_ad_text: str):
    order.approved = True
    order.final_ad_text = safe_html(final_ad_text)
    post_date = order.ad.extra_info.post_date or order.date
    post_date = max(time(), post_date)
    if order.ad.extra_info.pin and order.pin_from is None:
        order.pin_from = get_min_pin_date(order.channel_id) or post_date
        order.pin_until = order.pin_from + PIN_DURATION
    if order.ad.extra_info.duplicate:
        order.posts_dates = [
            post_date + i * DUPLICATE_INTERVAL for i in range(DUPLICATE_TIMES)
        ]
    else:
        order.posts_dates = [post_date]
    order.save()
    return order


# order = Order.find()
# print(order.id)
# print(approve_order(order, "123"))
# print(get_min_pin_date(-1001398658451))


def save_post(order: Order):
    post = Post()
    post.chat_id = order.channel_id
    post.text = order.final_ad_text
    post.pin_from = order.pin_from
    post.pin_until = order.pin_until
    post.publish_dates = order.posts_dates
    post.save()
    return post


def make_order(ad: Ad, channel_id: int, user_id: int, invoice: Invoice) -> Order:
    order = Order(
        user_id=str(user_id),
        ad=ad,
        date=time(),
        price=invoice.total_price,
        channel_id=channel_id,
        app_id=APP_ID,
        final_ad_text=repr_ad(ad),
    )
    return order.save()


def make_invoice(ad: Ad) -> Invoice:
    vacancy_amount = len(ad.vacancies)
    pin = ad.extra_info.pin
    duplicate = ad.extra_info.duplicate
    vacancies_price = PRICES.VACANCIES[vacancy_amount]
    pin_price = PRICES.PIN_OPTION if pin else 0
    duplicate_price = PRICES.DUPLICATE_OPTION[vacancy_amount] if duplicate else 0
    return Invoice(vacancies_price, pin_price, duplicate_price)


async def get_invoice_url(order: Order, bot_url: str) -> str:
    return await merchant.get_invoice_url(order.str_id, order.price, bot_url)


def get_my_order(user_id: int, index=0) -> Order | None:
    filters = {"user_id": str(user_id), "paid": True, "app_id": APP_ID}
    orders = Order.find_all(**filters)
    try:
        return orders[index]
    except IndexError:
        return None


def get_webhook_url(order: Order) -> str:
    wh = Webhook.get(order.app_id)
    return wh.url


def set_webhook():
    Webhook(app_id=APP_ID, url=APP_URL).save()


async def send_post(url: str, params: dict = None):
    session = ClientSession()
    async with session.post(url, params=params) as resp:
        resp.raise_for_status()
    await session.close()
    return resp


def make_ad_header(order: Order) -> str:
    return texts.NEW_ORDER.format(
        user_id=order.user_id,
        order_id=order.str_id,
        pinning="да" if order.ad.extra_info.pin else "нет",
        duplicating="да" if order.ad.extra_info.duplicate else "нет",
        post_date=repr_timestamp_as_date(order.ad.extra_info.post_date or order.date),
    )
