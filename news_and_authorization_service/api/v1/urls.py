"""URLs configuration of the 'Api' application v1."""

from django.urls import include, path

urlpatterns = [
    path("auth/", include("api.v1.auth.urls")),
    path("news/", include("api.v1.news.urls")),
    path("news/<int:pk_news>/comments/", include("api.v1.comments.urls")),
]
