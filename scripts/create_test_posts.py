from time import time

from mongo import Document
from mongoengine import BooleanField, StringField


class Post(Document):
    chat_id: int
    text: str
    pin_from: int | None
    pin_until: int | None
    publish_dates: list[int]
    message_id: int | None


time = time() + 10


def create_post(num: int):
    post = Post()
    post.chat_id = 724477101
    post.text = f"post{num}"
    post.pin_from = time
    post.pin_until = time + 10
    post.publish_dates = [time, time + 5, time + 15]
    post.save()


create_post(1)
create_post(2)
create_post(3)
