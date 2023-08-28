import re
from asyncio import get_event_loop, run
from time import time as get_time
from typing import Callable

from loader import bot, viber_bot
from loguru import logger

from api import Post

PostTaskCallback = Callable[[Post], None]


def process_post(post: Post):
    time = get_time()
    print(post.publish_dates, time, time >= post.publish_dates[0])
    if post.publish_dates and time >= post.publish_dates[0]:
        run_post_task(post, send_post)
    if post.pin_from and time >= post.pin_from:
        run_post_task(post, pin_post)
    if post.pin_until and time >= post.pin_until:
        run_post_task(post, unpin_post)
    if not (post.publish_dates or post.pin_from or post.pin_until):
        post.delete()


def run_post_task(post: Post, callback: PostTaskCallback):
    callback = logger.catch(reraise=True)(callback)
    for _ in range(3):
        try:
            callback(post)
            post.save()
            return
        except Exception:
            pass


def send_post(post: Post):
    msg = bot.send_message(post.chat_id, post.text)
    if not post.message_id:
        post.message_id = msg.message_id
    send_viber_post("Необходимо опубликовать пост:", post)
    post.publish_dates.pop(0)
    post.save()


def pin_post(post: Post):
    if not post.pin_from:
        return
    send_viber_post("Необходимо закрепить пост:", post)
    bot.pin_chat_message(post.chat_id, post.message_id)
    post.pin_from = None
    post.save()


def unpin_post(post: Post):
    if not post.message_id:
        return
    send_viber_post("Необходимо открепить пост:", post)
    bot.unpin_chat_message(post.chat_id, post.message_id)
    post.pin_until = None
    post.save()


def send_viber_post(header: str, post: Post):
    pattern = r'<a href="(.*)">.*</a>'
    r = re.search(pattern, post.text)
    photo_url = r.group(1)
    text = re.sub(pattern, "", post.text)
    text = re.sub("<b>", "*", text)
    text = re.sub("</b>", "*", text)
    send_viber_message(header)
    send_viber_picture(photo_url, text)


VIBER_CHAT_ID = "VXMh1WXcHdyFRdes7oaIEg=="


def send_viber_picture(url: str, text: str):
    loop = get_event_loop()
    loop.run_until_complete(viber_bot.send_picture(VIBER_CHAT_ID, url, text))


def send_viber_message(text: str):
    loop = get_event_loop()
    loop.run_until_complete(viber_bot.send_message(VIBER_CHAT_ID, text))
