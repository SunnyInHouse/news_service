"""ASGI config for news_and_authorization_service project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "news_and_authorization_service.settings"
)

application = get_asgi_application()
