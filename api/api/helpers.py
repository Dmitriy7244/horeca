import re
from datetime import datetime
from time import time

from .config import PRICES, APP_ID, APP_URL
from .merchant import merchant
from .models import Order, Ad, Invoice, Webhook


def safe_html(text: str) -> str:
    """Escape "<" and ">" symbols that are not a part of a tag."""
    return re.sub(
        pattern="<(?!(/|b>|i>|u>|s>|tg-spoiler>|a>|a href=|code>|pre>|code class=))",
        repl="&lt;",
        string=text,
    )


def uncapitalize(text: str):
    return text[0].lower() + text[1:]


def repr_timestamp_as_date(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M")


def approve_order(order: Order):
    order.approved = True
    order.save()


def make_order(ad: Ad, channel_id: int, user_id: int, invoice: Invoice) -> Order:
    order = Order(
        user_id=str(user_id),
        ad=ad,
        date=time(),
        price=invoice.total_price,
        channel_id=channel_id,
        app_id=APP_ID,
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


def get_min_pin_date(channel_id: int) -> int:
    filters = {"approved": True, "channel_id": channel_id}
    until_dates = [o.pin_until for o in Order.find_docs(**filters)]
    return max(until_dates) if until_dates else 0


def get_paid_order(user_id: int, index=0) -> Order | None:
    filters = {"user_id": str(user_id), "paid": True}
    orders = Order.find_docs(**filters)
    try:
        return orders[index]
    except IndexError:
        return None


def get_webhook_url(order: Order) -> str:
    wh = Webhook.get_doc(order.app_id)
    return wh.url


def set_webhook():
    Webhook(app_id=APP_ID, url=APP_URL).save()
