"""URL configuration for 'news_and_authorization_service' project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
