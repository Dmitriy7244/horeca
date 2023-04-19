import asyncio
import time

from viber import types
from viber.dispatcher import FSMContext

from models.ad import Invoice, Order
from ... import api0
from ... import config
from ... import kbs as kb
from ... import texts
from ...conversations.fill_ad import FillAd as Conv
from ...loader import dp, merchant
from src.utils import repr_invoice
from src.utils import AdProxy


@dp.message_handler(button=kb.ChangeAd.ALL_GOOD, state=Conv.preview_post)
async def send_invoice(message: types.Message, state: FSMContext):
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
            user_id=message.from_user.id,
            ad=ad,
            date=time.time(),
            price=invoice.total_price,
            created_from=config.BOT_URI,
            channel_id=await api0.get_channel_id_for_ad(),
        ).save()

    order_id = str(order.id)

    loop = asyncio.get_running_loop()
    payment_url = await loop.run_in_executor(
        None,
        merchant.get_invoice_url,
        order_id, order.price,
    )

    await state.finish()
    await message.answer(repr_invoice(invoice), reply_markup=kb.Payment(payment_url))
    # await message.answer(texts.send_me_start_command, reply_markup=kb.Payment(payment_url))
