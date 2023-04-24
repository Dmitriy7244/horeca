from api import models, config
from .storage_proxies import AdProxy


async def get_channel_id_for_ad(ad: models.Ad = None):
    ad = ad or await AdProxy().ad
    return config.get_channel(ad.company_info.region)


async def check_pinning_availability():
    channel_id = await get_channel_id_for_ad()
    until_dates = []

    for order in models.Order.objects(approved=True, channel_id=channel_id):
        order: models.Order
        if order.pin_until:
            until_dates.append(order.pin_until)

    return max(until_dates) if until_dates else 0
