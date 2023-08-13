from django.test import TestCase
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from ..serializer import CoinSerializer
from ..views import *
from ..models import Coin


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
    """Test module for GET all Coins API result"""

    def setUp(self):
        Coin.objects.create(
            name="bitcoin", abbreviation_name="BTC", purchase_price=3, sale_price=0
        )
        Coin.objects.create(
            name="cardano", abbreviation_name="ADA", purchase_price=2, sale_price=0
        )

    def test_get_all_coins_valid_status_code(self):
        factory = APIRequestFactory()
        view = CoinsViewSet.as_view({"get": "list"})
        request = factory.get("CoinsViewSet")
        Coins = Coin.objects.all()
        response = view(request)
        serializer = CoinSerializer(Coins, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_coins_valid_result(self):
        factory = APIRequestFactory()
        view = CoinsViewSet.as_view({"get": "list"})
        request = factory.get("CoinsViewSet")
        Coins = Coin.objects.all()
        response = view(request)
        serializer = CoinSerializer(Coins, many=True)
        self.assertEqual(serializer.data, response.data.get("results"))

    def test_get_all_coins_invalid_method(self):
        client = APIClient()
        request = client.post("/api/coin/coin/", data={})
        Coins = Coin.objects.all()
        self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
