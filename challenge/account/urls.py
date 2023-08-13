from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LoginApi, GetUserDetailApi


urlpatterns = [
    path("sign_in/", LoginApi.as_view()),
    path("user_detail/", GetUserDetailApi.as_view()),
]
