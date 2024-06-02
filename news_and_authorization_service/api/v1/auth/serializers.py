"""Serializers for the endpoints 'auth' of the 'Api' application v1."""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers

User = get_user_model()


class AuthUserSignInSerilizer(serializers.Serializer):
    """Serializer for working with signin requests."""

    username = serializers.CharField()
    password = serializers.CharField()

    default_error_messages = {
        "invalid_password": "Invalid password.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        self.user = get_object_or_404(User, username=username)

        if not check_password(password, self.user.password):
            raise serializers.ValidationError(
                {"detail": self.error_messages["invalid_password"]}
            )

        return data
