"""Views decorators for use in documentation."""

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status

from api.v1.auth.serializers import AuthUserSignInSerilizer
from api.v1.comments.serializers import CommentSerializer
from api.v1.likes.serializers import LikeSerializer
from api.v1.drf_spectacular.serializers import (
    Response200TokensSerializer,
    Response400Serializer,
    Response401Serializer,
    Response403Serializer,
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
    "CommentsViewSet": extend_schema_view(
        create=extend_schema(
            tags=("comments",),
            responses={
                status.HTTP_201_CREATED: CommentSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        list=extend_schema(
            tags=("comments",),
            responses={
                status.HTTP_200_OK: CommentSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        retrieve=extend_schema(
            tags=("comments",),
            responses={
                status.HTTP_200_OK: CommentSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        destroy=extend_schema(
            tags=("comments",),
            responses={
                status.HTTP_204_NO_CONTENT: OpenApiResponse(response=None),
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_403_FORBIDDEN: Response403Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
    "LikesViewSet": extend_schema_view(
        create=extend_schema(
            tags=("likes",),
            responses={
                status.HTTP_201_CREATED: LikeSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        list=extend_schema(
            tags=("likes",),
            responses={
                status.HTTP_200_OK: LikeSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        retrieve=extend_schema(
            tags=("likes",),
            responses={
                status.HTTP_200_OK: LikeSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        destroy=extend_schema(
            tags=("likes",),
            responses={
                status.HTTP_204_NO_CONTENT: OpenApiResponse(response=None),
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_403_FORBIDDEN: Response403Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
    "NewsViewSet": extend_schema_view(
        create=extend_schema(
            tags=("news",),
            responses={
                status.HTTP_201_CREATED: LikeSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        list=extend_schema(
            tags=("news",),
            responses={
                status.HTTP_200_OK: LikeSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        retrieve=extend_schema(
            tags=("news",),
            responses={
                status.HTTP_200_OK: LikeSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        update=extend_schema(
            tags=("news",),
            responses={
                status.HTTP_200_OK: LikeSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_403_FORBIDDEN: Response403Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        destroy=extend_schema(
            tags=("news",),
            responses={
                status.HTTP_204_NO_CONTENT: OpenApiResponse(response=None),
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_403_FORBIDDEN: Response403Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
