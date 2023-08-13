from rest_framework import serializers
from django.db import transaction
from django.db.models import Sum


from account.serializers import UserProfileSerializer
from coin.serializer import CoinSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "user" "coin",
            "purchase_price",
            "sale_price",
            "total_price",
            "external_checkout",
            "amount",
        ]


class ByCryptoSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    sale_price = serializers.DecimalField(
        read_only=True, decimal_places=2, max_digits=18
    )
    total_price = serializers.DecimalField(
        read_only=True, decimal_places=2, max_digits=18
    )
    coin = CoinSerializer(read_only=True)
    coin_name = serializers.CharField()

    class Meta:
        model = Order
        fields = [
            "user" "coin",
            "purchase_price",
            "sale_price",
            "total_price",
            "external_checkout",
            "amount",
        ]
