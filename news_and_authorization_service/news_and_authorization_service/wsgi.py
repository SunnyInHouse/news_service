"""WSGI config for news_and_authorization_service project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "news_and_authorization_service.settings"
)

application = get_wsgi_application()
