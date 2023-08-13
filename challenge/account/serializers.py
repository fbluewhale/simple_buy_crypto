import pytz
import datetime
from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import UserProfile, DjangoUser
from utils.exceptions import ValidationException


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get("request"),
            username=attrs["username"],
            password=attrs["password"],
        )

        if not user:
            raise ValidationException("username or password number is wrong")

        user_profile = UserProfile.get_or_404(user=user)
        return user_profile


class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser
        fields = [
            "username",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = UserProfile
        fields = (
            "balance",
            "user",
        )

    def to_representation(self, instance):
        data = super(UserProfileSerializer, self).to_representation(instance)
        profile = data.pop("user")

        for key, val in profile.items():
            data.update({key: val})

        return data
