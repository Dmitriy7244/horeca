from mongo import Document
from mongoengine import BooleanField, StringField


class Order(Document):
    meta = {"strict": False}
    created_from: str = StringField()
    app_id: str = StringField()
    paid_up: bool = BooleanField()
    paid: bool = BooleanField()
    utm: str = StringField()


count = 0


def migrate_paid_field():
    for order in Order.find_all():
        if order.paid_up is None:
            continue
        order.paid = order.paid_up
        order.paid_up = None
        order.save()


def migrate_create_from_field():
    for order in Order.find_all():
        # if order.created_from is None:
        # continue
        # order.app_id = order.created_from.replace(".", "-")
        # order.created_from = None

        if order.app_id == "telegram-ru":
            order.app_id = "tg-ru"
        if order.app_id == "telegram-ua":
            order.app_id = "tg-ua"
        order.save()


migrate_create_from_field()
