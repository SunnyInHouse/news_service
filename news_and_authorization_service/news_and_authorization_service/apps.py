"""Configuration of 'Admin' application."""

from django.contrib.admin.apps import AdminConfig


class NewsAndAuthorizationServiceAdminConfig(AdminConfig):
    """Settings of admin site."""

    default_site = (
        "news_and_authorization_service.admin.NewsAndAuthorizationServiceAdminSite"
    )
