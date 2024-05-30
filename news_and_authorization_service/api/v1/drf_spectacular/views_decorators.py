"""Views decorators for use in documentation."""

from drf_spectacular.utils import extend_schema
from rest_framework import status

from api.v1.auth.serializers import AuthUserSignInSerilizer
from api.v1.drf_spectacular.serializers import (
    Response200TokensSerializer,
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)


VIEWS_DECORATORS = {
    "signin": extend_schema(
        tags=("auth",),
        request=AuthUserSignInSerilizer,
        responses={
            status.HTTP_200_OK: Response200TokensSerializer,
            status.HTTP_400_BAD_REQUEST: Response400Serializer,
            status.HTTP_404_NOT_FOUND: Response404Serializer,
        },
    ),
}
