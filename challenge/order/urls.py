from django.urls import include, path
from .views import BuyCryptoSyncApi, BuyCryptoAsyncApi


urlpatterns = [
    path("set_order/", BuyCryptoSyncApi.as_view()),
    path("set_order_async/", BuyCryptoAsyncApi.as_view()),
]
