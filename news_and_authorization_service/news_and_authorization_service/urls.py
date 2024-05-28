"""URL configuration for 'news_and_authorization_service' project."""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
