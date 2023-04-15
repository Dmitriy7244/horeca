import asyncio
import time

from aiogram.types import ReplyKeyboardRemove
from aiogram_tools.context import message, storage

from loader import merchant
from models.ad import Invoice, Order
from ... import api
from ... import config
from ... import keyboards as kb
from ... import texts
from ...conversations.fill_ad import FillAd as Conv
from ...loader import dp
from ...utils.repr import repr_invoice
from ...utils.storage_proxies import AdProxy


@dp.message_handler(button=kb.ChangeAd.ALL_GOOD, state=Conv.preview_post)
async def send_invoice(_):
    async with AdProxy() as ad:
        vacancies_amount = len(ad.vacancies)
        pinning = ad.extra_info.pin
        duplicating = ad.extra_info.duplicate

    vacancies_price = config.VACANCIES_PRICES[vacancies_amount]
    pinning_price = config.PINNING_PRICE if pinning else 0
    duplicating_price = config.DUPLICATING_PRICES[vacancies_amount] if duplicating else 0
    invoice = Invoice(vacancies_price, pinning_price, duplicating_price)

    async with AdProxy() as ad:
        order = Order(
            user_id=str(message.from_user.id),
            ad=ad,
            date=time.time(),
            price=invoice.total_price,
            created_from=config.BOT_URI,
            channel_id=await api.get_channel_id_for_ad(),
        ).save()

    order_id = str(order.id)
    bot_url = await api.get_bot_url()

    loop = asyncio.get_running_loop()
    payment_url = await loop.run_in_executor(
        None,
        merchant.get_invoice_url,
        order_id, order.price, bot_url
    )

    await storage.finish()
    await message.answer(repr_invoice(invoice), reply_markup=kb.Payment(payment_url))
    # await message.answer(texts.send_me_start_command, reply_markup=ReplyKeyboardRemove())