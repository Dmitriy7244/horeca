from api.core import Document
from mongoengine import StringField, BooleanField


class Order(Document):
    meta = {"strict": False}
    created_from: str = StringField()
    app_id: str = StringField()
    paid_up: bool = BooleanField()
    paid: bool = BooleanField()
    utm: str = StringField()


for order in Order.find_docs():
    order.paid = order.paid_up
    order.paid_up = None

    if order.created_from:
        order.app_id = order.created_from.replace(".", "-")
        order.created_from = None

    order.save()
