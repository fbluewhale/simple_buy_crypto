from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CoinsViewSet

router = DefaultRouter()
router.register(r"coin", CoinsViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
