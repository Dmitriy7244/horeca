from time import time as get_time
from typing import Callable

from loader import bot
from loguru import logger

from api import Post

PostTaskCallback = Callable[[Post], None]


def process_post(post: Post):
    time = get_time()
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
    post.publish_dates.pop(0)
    post.save()


def pin_post(post: Post):
    if not post.pin_from:
        return
    bot.pin_chat_message(post.chat_id, post.message_id)
    post.pin_from = None
    post.save()


def unpin_post(post: Post):
    if not post.message_id:
        return
    bot.unpin_chat_message(post.chat_id, post.message_id)
    post.pin_until = None
    post.save()
