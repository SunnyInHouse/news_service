"""Serializers describing responses for use in documentation."""

from rest_framework import serializers


class Response200TokensSerializer(serializers.Serializer):
    """200 response: Tokens."""

    access = serializers.CharField()
    refresh = serializers.CharField()


class ResponseErrorSerializer(serializers.Serializer):
    """Response with errors."""

    message = serializers.CharField(
        default="",
    )
    debug_information = serializers.CharField(
        default="api_error",
    )


class Response400Serializer(ResponseErrorSerializer):
    """400 response: Invalid field value."""

    message = serializers.CharField(
        default="FieldValidationError",
    )


class Response401Serializer(ResponseErrorSerializer):
    """400 response: Invalid field value."""

    message = serializers.CharField(
        default="AuthenticationFailed",
    )


class Response404Serializer(ResponseErrorSerializer):
    """404 response: Not found."""

    message = serializers.CharField(
        default="DataNotFound",
    )
