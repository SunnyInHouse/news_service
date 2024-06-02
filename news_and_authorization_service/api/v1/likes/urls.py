"""URLs configuration of the endpoints 'likes' to news of the 'Api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.likes.views import LikesViewSet

router_likes_v1 = DefaultRouter()

router_likes_v1.register("", LikesViewSet, basename="likes")

urlpatterns = [
    path("", include(router_likes_v1.urls)),
]
