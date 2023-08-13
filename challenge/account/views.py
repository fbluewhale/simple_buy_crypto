from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from .models import UserProfile


# Create your views here.
class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginApi(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user_serializer = UserProfileSerializer(user)
        token, _ = Token.objects.get_or_create(user=user.user)
        return Response(data={**user_serializer.data, "token": token.key}, status=201)


class GetUserDetailApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        user_serializer = UserProfileSerializer(user_profile)
        return Response(user_serializer.data)
