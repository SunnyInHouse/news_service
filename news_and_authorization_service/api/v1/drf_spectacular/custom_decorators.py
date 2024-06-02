"""Custom decorators for drf-spectacular."""

from django.conf import settings


def activate_drf_spectacular_view_decorator(view):
    """Select a view decorator for the specified view."""
    if settings.DEBUG:
        from api.v1.drf_spectacular.views_decorators import VIEWS_DECORATORS

        view_name = (
            view.view_class.__name__
            if view.__class__.__name__ == "function"
            else view.__name__
        )
        return VIEWS_DECORATORS[view_name](view)

    return view
