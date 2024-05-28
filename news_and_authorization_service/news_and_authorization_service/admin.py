"""Module provides application administration functionality."""

from django.contrib import admin


class NewsAndAuthorizationServiceAdminSite(admin.AdminSite):
    """Custom admin site."""

    site_header = "News and Authorization Service. Admin Site."
    site_title = "News And Authorization Service."
