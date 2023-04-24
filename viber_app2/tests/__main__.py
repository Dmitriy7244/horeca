from aiohttp import ClientSession
import asyncio

json = {
    "rrn": "111111111111",
    "masked_card": "444455XXXXXX1111",
    "sender_cell_phone": "",
    "sender_account": "",
    "currency": "UAH",
    "fee": "",
    "reversal_amount": "0",
    "settlement_amount": "0",
    "actual_amount": "200000",
    "response_description": "",
    "sender_email": "levchenko.d.a1998@gmail.com",
    "order_status": "approved",
    "response_status": "success",
    "order_time": "16.04.2023 16:58:19",
    "actual_currency": "UAH",
    "order_id": "643da506e0f1cad6b439c1fc",
    "tran_type": "purchase",
    "eci": "5",
    "settlement_date": "",
    "payment_system": "card",
    "approval_code": "123456",
    "merchant_id": 1396424,
    "settlement_currency": "",
    "payment_id": 565679722,
    "card_bin": 444455,
    "response_code": "",
    "card_type": "VISA",
    "amount": "200000",
    "signature": "62602e4f2b049e5490dd1a95147d18d97e5553ec",
    "product_id": "",
    "merchant_data": "",
    "rectoken": "",
    "rectoken_lifetime": "",
    "verification_status": "",
    "parent_order_id": "",
    "response_signature_string": "**********|200000|UAH|200000|123456|444455|VISA|UAH|5|444455XXXXXX1111|1396424|643bfefb258f9a24b6103e90|approved|16.04.2023 16:58:19|565679722|card|success|0|111111111111|levchenko.d.a1998@gmail.com|0|purchase",
}


async def main():
    session = ClientSession("http://localhost")
    async with session.post("/payment", json=json) as resp:
        result = await resp.text()
        print(result)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
