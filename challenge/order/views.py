from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from utils.utils import validate_serializer
from .serializer import ByCryptoSerializer, OrderSerializer
from .helper import create_async_order, create_sync_order

# Create your views here.


class BuyCryptoSyncApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(request_body=ByCryptoSerializer)
    @validate_serializer(ByCryptoSerializer)
    def post(self, request):
        serializer = ByCryptoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = create_sync_order(serializer.validated_data, request)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class BuyCryptoAsyncApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(request_body=ByCryptoSerializer)
    @validate_serializer(ByCryptoSerializer)
    def post(self, request):
        serializer = ByCryptoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = create_async_order(serializer.validated_data, request)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
