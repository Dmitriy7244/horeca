import time

from api import models, PRICES, merchant, repr_invoice
from botty import Message, dp, reply, bot

from assets import kbs, CreateAdStates
from lib import AdProxy, get_channel_id_for_ad


@dp.text(kbs.EditAd.DONE, CreateAdStates.EDIT)
async def _(msg: Message):
    invoice = await make_invoice()
    order = await make_order(msg, invoice)

    # await state.finish() # TODO
    url = await merchant.get_invoice_url(str(order.id), order.price, await bot.url)
    await reply(msg, repr_invoice(invoice), kbs.Invoice(url))


async def make_invoice() -> models.Invoice:
    async with AdProxy() as ad:
        vacancy_amount = len(ad.vacancies)
        pin = ad.extra_info.pin
        duplicate = ad.extra_info.duplicate

    vacancies_price = PRICES.VACANCIES[vacancy_amount]
    pin_price = PRICES.PIN_OPTION if pin else 0
    duplicate_price = PRICES.DUPLICATE_OPTION[vacancy_amount] if duplicate else 0
    return models.Invoice(vacancies_price, pin_price, duplicate_price)


async def make_order(msg, invoice: models.Invoice) -> models.Order:
    ad = await AdProxy().ad
    order = models.Order(
        user_id=str(msg.from_user.id),
        ad=ad,
        date=time.time(),
        price=invoice.total_price,
        channel_id=await get_channel_id_for_ad(),
    )
    return order.save()
