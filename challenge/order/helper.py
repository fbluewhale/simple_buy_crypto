from django.db import transaction
from django.db.models import Sum

from utils.exceptions import ValidationException
from utils.utils import buy_from_exchange
from account.models import UserProfile
from coin.models import Coin
from .models import Order


def check_coin_price_with_purchase_price(coin_name, purchase_price):
    coin = Coin.get_or_404(abbreviation_name=coin_name)
    if purchase_price != coin.purchase_price:
        raise ValidationException("purchase_price is not valid")


def create_async_order(validated_data, request):
    with transaction.atomic():
        user_profile = UserProfile.objects.get(user=request.user)

        coin = Coin.get_or_404(abbreviation_name=validated_data.pop("coin_name"))
        purchase_price = validated_data.get("purchase_price")
        check_coin_price_with_purchase_price(coin.abbreviation_name, purchase_price)

        total_price = validated_data.get("amount") * purchase_price
        order = Order.objects.create(
            **validated_data, user=user_profile, total_price=total_price, coin=coin
        )

        unexchanged_order = Order.objects.select_for_update().filter(
            external_checkout=False, coin=coin
        )
        unexchanged_order_total_price = unexchanged_order.aggregate(Sum("total_price"))
        return order


def create_sync_order(validated_data, request):
    with transaction.atomic():
        user_profile = UserProfile.get_or_404(user=request.user)

        coin = Coin.get_or_404(abbreviation_name=validated_data.pop("coin_name"))
        purchase_price = validated_data.get("purchase_price")
        check_coin_price_with_purchase_price(coin.abbreviation_name, purchase_price)

        total_price = validated_data.get("amount") * purchase_price
        order = Order.objects.create(
            **validated_data, user=user_profile, total_price=total_price, coin=coin
        )

        unexchanged_order = Order.objects.select_for_update().filter(
            external_checkout=False, coin=coin
        )
        unexchanged_order_total_price = unexchanged_order.aggregate(Sum("total_price"))
        if unexchanged_order_total_price.get("total_price__sum") >= 10:
            total_amount = unexchanged_order.aggregate(Sum("amount")).get(
                "total_amount__sum"
            )
            buy_from_exchange(validated_data.get("coin"), total_amount)
            unexchanged_order.update(external_checkout=True)

        return order
