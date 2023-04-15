import asyncio
import ssl

import mongoengine
from aiohttp import web

import app_telegram_ru
import app_telegram_ua
import app_viber_ru
import app_viber_ua
import config
import payment_handler
import poster

mongoengine.connect(config.MAIN_DB_NAME)

dp_ru = app_telegram_ru.loader.dp
dp_ua = app_telegram_ua.loader.dp

dp_viber_ru = app_viber_ru.loader.dp
dp_viber_ua = app_viber_ua.loader.dp


def configure_app(_app: web.Application, dp, route_path, route_name):
    from aiogram import Dispatcher, Bot
    from aiogram.dispatcher.webhook import WebhookRequestHandler

    dp: Dispatcher

    class NewWebhookRequestHandler(WebhookRequestHandler):

        def get_dispatcher(self):
            try:
                Dispatcher.set_current(dp)
                Bot.set_current(dp.bot)
            except RuntimeError:
                pass
            return dp

    _app.router.add_route('*', route_path, NewWebhookRequestHandler, name=route_name)


def configure_viber_app(app: web.Application, dp, route_path, route_name):
    from aioviber2 import Dispatcher, Bot
    from aioviber2.dispatcher.webhook import WebhookRequestHandler

    class NewWebhookRequestHandler(WebhookRequestHandler):

        def get_dispatcher(self):
            try:
                Dispatcher.set_current(dp)
                Bot.set_current(dp.bot)
            except RuntimeError:
                pass
            return dp

    app.router.add_route('*', route_path, NewWebhookRequestHandler, name=route_name)


app = web.Application()
configure_app(app, dp_ru, '/telegram/ru', 'telegram.ru')
configure_app(app, dp_ua, '/telegram/ua', 'telegram.ua')
configure_viber_app(app, dp_viber_ru, '/viber/ru', 'viber.ru')
configure_viber_app(app, dp_viber_ua, '/viber/ua', 'viber.ua')
app.router.add_post(config.PAYMENT_PATH, payment_handler.process_payment)


async def main():
    await dp_ru.bot.set_webhook(config.HOST + '/telegram/ru')
    await dp_ua.bot.set_webhook(config.HOST + '/telegram/ua')
    await dp_viber_ru.bot.set_webhook(config.HOST + '/viber/ru')
    await dp_viber_ua.bot.set_webhook(config.HOST + '/viber/ua')


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.create_task(poster.check_forever())

try:
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(config.SSL_CERT_FILE, config.SSL_KEY_FILE)
except:
    web.run_app(app)
else:
    web.run_app(app, port=8443, ssl_context=ssl_context, reuse_port=True)
