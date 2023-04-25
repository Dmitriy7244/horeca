import api
from api import repr_invoice, Order, Invoice, get_invoice_url, texts

from assets import kbs, CreateAdStates
from deps import Message, dp, reply, bot, FSMContext, VIBER_MODE
from lib import AdProxy, get_channel_id_for_ad


@dp.text(kbs.EditAd.DONE).state(CreateAdStates.EDIT)
async def _(msg: Message, state: FSMContext):
    # await state.finish() # TODO
    invoice = await make_invoice()
    order = await make_order(msg, invoice)
    bot_url = None if VIBER_MODE else await bot.url
    url = await get_invoice_url(order, bot_url)
    await reply(msg, texts.ORDER_CREATED, markup=False)
    await reply(msg, repr_invoice(invoice), kbs.Invoice(url))


async def make_invoice() -> Invoice:
    ad = await AdProxy().ad
    return api.make_invoice(ad)


async def make_order(msg: Message, invoice: Invoice) -> Order:
    ad = await AdProxy().ad
    channel_id = await get_channel_id_for_ad()
    return api.make_order(ad, channel_id, msg.from_user.id, invoice)
