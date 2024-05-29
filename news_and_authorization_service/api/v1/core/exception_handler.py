"""Api exception handler of the 'development_tracker' application."""

from django.conf import settings
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    """Handle of API Exception."""
    handlers = {
        "AuthenticationFailed": _handle_authentication_failed,
        "PermissionDenied": _handle_permission_denied,
        "ValidationError": _handle_validation_error,
        "Http404": _handle_not_found,
    }

    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__

    if response is None:
        response = Response(
            data="InternalServerError",
            content_type="application/json",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    else:
        response.data = ""

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return _handle_generic_error(exc, context, response)


def _handle_generic_error(exc, context, response):
    """Generate response from all handlers."""
    if "message" not in response.data:
        response.data = {"message": response.data}

    debug_info = (
        str(exc) if (not exc.__dict__ or "detail" not in exc.__dict__) else exc.detail
    )

    if settings.DEBUG is True:
        response.data.update(
            {
                "debug_information": debug_info,
            }
        )

    headers = {}
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

    return Response(response.data, status=response.status_code, headers=headers)


def _handle_authentication_failed(exc, context, response):
    """Handle of Authentication Failed Error."""
    response.status_code = status.HTTP_401_UNAUTHORIZED
    response.data = "AuthenticationFailed"
    return _handle_generic_error(exc, context, response)


def _handle_permission_denied(exc, context, response):
    """Handle of Permission Denied Error."""
    response.status_code = status.HTTP_403_FORBIDDEN
    response.data = exc.get_full_details()["code"]
    return _handle_generic_error(exc, context, response)


def _handle_validation_error(exc, context, response):
    """Handle of Validation Error."""
    response.status_code = status.HTTP_400_BAD_REQUEST
    response.data = "FieldValidationError"
    return _handle_generic_error(exc, context, response)


def _handle_not_found(exc, context, response):
    """Handle of NotFound Error."""
    response.status_code = status.HTTP_404_NOT_FOUND
    response.data = "DataNotFound"
    return _handle_generic_error(exc, context, response)
