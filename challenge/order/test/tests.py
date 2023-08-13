from django.test import TestCase
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from coin.models import Coin
from account.models import UserProfile, DjangoUser
from ..serializer import CoinSerializer, ByCryptoSerializer, OrderSerializer
from ..views import BuyCryptoAsyncApi
from ..models import Order


class OrderTest(TestCase):
    """Test buy coin"""

    def setUp(self):
        coin_1 = Coin.objects.create(
            name="bitcoin", abbreviation_name="BTC", purchase_price=3, sale_price=0
        )
        django_user = DjangoUser.objects.create(username="ali", password="1234")
        user = UserProfile.objects.create(user=django_user)
        # self.client.force_authenticate(user=django_user)

    def test_creation_coin_valid_status(self):
        user = UserProfile.objects.get(user=DjangoUser.objects.get(username="ali"))
        token, _ = Token.objects.get_or_create(user=user.user)
        client = APIRequestFactory()
        request = client.post(
            "BuyCryptoAsyncApi",
            {"coin_name": "BTC", "purchase_price": 3, "amount": 2},
            format="json",
            headers={"AUTHORIZATION": "Token " + token.key},
        )
        view = BuyCryptoAsyncApi.as_view()
        response = view(
            request,
        )
        order = Order.objects.get(user=user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creation_coin_valid_result(self):
        user = UserProfile.objects.get(user=DjangoUser.objects.get(username="ali"))
        token, _ = Token.objects.get_or_create(user=user.user)
        client = APIRequestFactory()
        request = client.post(
            "BuyCryptoAsyncApi",
            {"coin_name": "BTC", "purchase_price": 3, "amount": 2},
            format="json",
            headers={"AUTHORIZATION": "Token " + token.key},
        )
        view = BuyCryptoAsyncApi.as_view()
        response = view(
            request,
        )
        order = Order.objects.get(user=user)

        self.assertEqual(OrderSerializer(order).data, response.data)
