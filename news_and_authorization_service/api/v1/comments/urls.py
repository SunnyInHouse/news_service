"""URLs configuration of the endpoints 'comments' to news of the 'Api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.comments.views import CommentsViewSet

router_comments_v1 = DefaultRouter()

router_comments_v1.register("", CommentsViewSet, basename="comments")

urlpatterns = [
    path("", include(router_comments_v1.urls)),
]
