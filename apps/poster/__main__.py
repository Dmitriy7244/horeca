from time import sleep

from lib import process_post
from loguru import logger

from api import Post

logger.info("Poster started")

while True:
    for post in Post.find_all():
        process_post(post)
        sleep(10)
