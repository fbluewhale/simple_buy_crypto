from django.test import TestCase
from ..models import Coin
from rest_framework import status
from django.test import TestCase
from ..serializer import CoinSerializer
from ..views import *
from rest_framework.test import APIRequestFactory


class CoinTest(TestCase):
    """Test module for Coin model"""

    def setUp(self):
        Coin.objects.create(
            name="bitcoin", abbreviation_name="BTC", purchase_price=3, sale_price=0
        )
        Coin.objects.create(
            name="cardano", abbreviation_name="ADA", purchase_price=2, sale_price=0
        )

    def test_creation_coin(self):
        Coin_1 = Coin.objects.get(name="bitcoin")
        Coin_2 = Coin.objects.get(abbreviation_name="ADA")
        self.assertEqual(Coin_1.purchase_price, 3)
        self.assertEqual(Coin_2.purchase_price, 2)


class GetAllCoinTest(TestCase):
    """Test module for GET all Coins API"""

    def setUp(self):
        Coin.objects.create(
            name="bitcoin", abbreviation_name="BTC", purchase_price=3, sale_price=0
        )
        Coin.objects.create(
            name="cardano", abbreviation_name="ADA", purchase_price=2, sale_price=0
        )

    def test_get_all_coins(self):
        factory = APIRequestFactory()
        view = CoinsViewSet.as_view({"get": "list"})
        request = factory.get("CoinsViewSet")
        Coins = Coin.objects.all()
        response = view(request)
        serializer = CoinSerializer(Coins, many=True)
        self.assertEqual(serializer.data, response.data.get("results"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
