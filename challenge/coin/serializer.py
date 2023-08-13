import pytz
import datetime
from rest_framework import serializers
from django.db import transaction
from django.db.models import Sum

from account.serializers import UserProfileSerializer
from .models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = [
            "name",
            "abbreviation_name",
            "purchase_price",
            "sale_price",
        ]
