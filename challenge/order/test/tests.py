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
    """Test buy coinw"""

    def setUp(self):
        coin_1 = Coin.objects.create(
            name="bitcoin", abbreviation_name="BTC", purchase_price=3, sale_price=0
        )
        django_user = DjangoUser.objects.create(username="ali", password="1234")
        user = UserProfile.objects.create(user=django_user)
        # self.client.force_authenticate(user=django_user)

    def test_creation_coin(self):
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetAllCoinTest(TestCase):
#     """Test module for GET all Coins API"""

#     def setUp(self):
#         Coin.objects.create(
#             name="bitcoin", abbreviation_name="BTC", purchase_price=3, sale_price=0
#         )
#         Coin.objects.create(
#             name="cardano", abbreviation_name="ADA", purchase_price=2, sale_price=0
#         )

#     def test_get_all_coins(self):
#         factory = APIRequestFactory()
#         view = CoinsViewSet.as_view({"get": "list"})
#         request = factory.get("CoinsViewSet")
#         Coins = Coin.objects.all()
#         response = view(request)
#         serializer = CoinSerializer(Coins, many=True)
#         self.assertEqual(serializer.data, response.data.get("results"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
