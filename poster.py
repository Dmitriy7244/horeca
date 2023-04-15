from __future__ import annotations

import asyncio
import time

import app_telegram_ru
from app_telegram_ru.loader import log
from models.ad import Order

bot = app_telegram_ru.dp.bot


def get_active_orders() -> list[Order]:
    orders = []
    for order in Order.objects():
        if order.approved:
            orders.append(order)
    return orders


# noinspection PyTypeChecker
async def check_forever():
    while True:
        for order in get_active_orders():
            order: Order

            await bot.get_session()  # ?

            epoch = time.time()
            if order.posts_dates and epoch >= order.posts_dates[0]:
                order.posts_dates.pop(0)
                try:
                    post = await bot.send_message(order.channel_id, order.final_ad_text)
                except Exception as e:
                    log.exception(f'cannot post to channel: {order.channel_id}: {e}')
                else:
                    if not order.post_id:
                        order.post_id = post.message_id

            if order.pin_from and epoch >= order.pin_from:
                if not order.pinned:
                    try:
                        await bot.pin_chat_message(order.channel_id, order.post_id)
                    except Exception as e:
                        log.exception(f'cannot pin in channel: {order.channel_id}: {e}')

                    order.pinned = True

            if order.pin_until and epoch >= order.pin_until:
                if order.post_id:
                    try:
                        await bot.unpin_chat_message(order.channel_id, order.post_id)
                    except Exception as e:
                        log.exception(f'cannot unpin in channel: {order.channel_id}: {e}')

                order.pin_from = None
                order.pin_until = None
                order.pinned = False

            order.save()

        await asyncio.sleep(3)
