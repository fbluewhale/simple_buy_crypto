import datetime
import io
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema
from .serializer import CoinSerializer
from .models import Coin


class CoinsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    This viewset automatically provides `list` actions to get all coins detail
    """

    decorators = [swagger_auto_schema(responses=Coin)]
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
