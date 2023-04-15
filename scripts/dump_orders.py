import json

import mongoengine

from config import MAIN_DB_NAME
from models.ad import Order

mongoengine.connect(MAIN_DB_NAME)

orders = []

for o in Order.objects:
    o: Order
    o: dict = json.loads(o.to_json())
    orders.append(o)

with open('orders.json', 'w', encoding='utf-8') as fp:
    json.dump(orders, fp, ensure_ascii=False, indent=2)
