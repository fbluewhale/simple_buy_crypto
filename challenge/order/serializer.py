from rest_framework import serializers
from django.db import transaction
from django.db.models import Sum


from account.serializers import UserProfileSerializer
from coin.serializer import CoinSerializer
from .models import Order


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
