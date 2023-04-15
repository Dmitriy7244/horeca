import logging

import mongoengine

from .config import MONGO

logger = logging.getLogger()

mongoengine.connect(
    db=MONGO.DB,
    host=MONGO.HOST,
    username=MONGO.USER,
    password=MONGO.PASSWORD,
)
