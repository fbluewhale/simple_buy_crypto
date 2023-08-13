import logging
from celery import shared_task
from django.db.models import Sum
from order.models import Order
from utils.utils import buy_from_exchange


@shared_task
def external_checkout():
    unexchanged_order = Order.objects.select_for_update().filter(
        external_checkout=False
    )
    coins = unexchanged_order.values("coin").distinct()
    for coin in coins:
        unexchanged_order_total_price = unexchanged_order.aggregate(Sum("total_price"))
        if unexchanged_order_total_price.get("total_price__sum") >= 10:
            total_amount = unexchanged_order.aggregate(Sum("amount")).get(
                "total_amount__sum"
            )
            result = buy_from_exchange(coin, total_amount)
            unexchanged_order.update(external_checkout=True)
