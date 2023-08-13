import pytz
import datetime
from rest_framework import serializers
from django.db import transaction
from django.db.models import Sum

from .models import Order
from utils.exceptions import ValidationException
from utils.utils import buy_from_exchange
from account.serializers import UserProfileSerializer
from account.models import UserProfile
from coin.serializer import CoinSerializer
from coin.models import Coin
import time


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ByCryptoSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    sale_price = serializers.IntegerField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    coin = CoinSerializer(read_only=True)
    coin_name = serializers.CharField()

    class Meta:
        model = Order
        fields = "__all__"
        # validators = [DateBeforeValidator()]

    def create_async(self, validated_data, request):
        with transaction.atomic():
            user_profile = UserProfile.objects.get(user=request.user)

            coin = Coin.get_or_404(abbreviation_name=validated_data.pop("coin_name"))
            total_price = validated_data.get("amount") * validated_data.get(
                "purchase_price"
            )
            order = Order.objects.create(
                **validated_data, user=user_profile, total_price=total_price, coin=coin
            )

            unexchanged_order = Order.objects.select_for_update().filter(
                external_checkout=False, coin=coin
            )
            unexchanged_order_total_price = unexchanged_order.aggregate(
                Sum("total_price")
            )
            return order

    def create_sync(self, validated_data, request):
        with transaction.atomic():
            user_profile = UserProfile.get_or_404(user=request.user)

            coin = Coin.get_or_404(abbreviation_name=validated_data.pop("coin_name"))
            total_price = validated_data.get("amount") * validated_data.get(
                "purchase_price"
            )
            order = Order.objects.create(
                **validated_data, user=user_profile, total_price=total_price, coin=coin
            )

            unexchanged_order = Order.objects.select_for_update().filter(
                external_checkout=False, coin=coin
            )
            unexchanged_order_total_price = unexchanged_order.aggregate(
                Sum("total_price")
            )
            # time.sleep(10)
            if unexchanged_order_total_price.get("total_price__sum") >= 10:
                total_amount = unexchanged_order.aggregate(Sum("amount")).get(
                    "total_amount__sum"
                )
                buy_from_exchange(validated_data.get("coin"), total_amount)
                unexchanged_order.update(external_checkout=True)

                # return "order"
            return order

    def validate(self, data):
        coin = Coin.get_or_404(abbreviation_name=data.get("coin_name"))
        if data["purchase_price"] != coin.purchase_price:
            raise ValidationException("purchase_price is not valid")
        return data
