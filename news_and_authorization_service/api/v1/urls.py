"""URLs configuration of the 'Api' application v1."""

from django.urls import include, path

urlpatterns = [
    path("auth/", include("api.v1.auth.urls")),
    path("news/<int:news_id>/comments/", include("api.v1.comments.urls")),
    path("news/<int:news_id>/likes/", include("api.v1.likes.urls")),
    path("news/", include("api.v1.news.urls")),
]
