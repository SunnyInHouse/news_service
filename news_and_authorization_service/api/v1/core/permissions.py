"""Permissions for the 'Api' application v1."""

from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class IsUserOwner(IsAuthenticated):
    """Only authenticated requests from users who is owner of object."""

    message = "Available only for authenticated users who is owner of object."
    code = "OnlyOwnerOfObject"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsUserAdmin(IsAuthenticated):
    """Only authenticated requests from users-admins."""

    message = "Available only for authenticated users-admins."
    code = "OnlyAdmins"

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin


class IsUserReadOnly(IsAuthenticated):
    """Only authenticated requests from users to read."""

    message = "Available only for authenticated users to read."
    code = "OnlyRead"

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsUserNewsAuthor(IsAuthenticated):
    """Only authenticated requests from  user-owners of news."""

    message = "Available only for authenticated  user-owners of news."
    code = "OnlyOwnersOfNews"

    def has_object_permission(self, request, view, obj):
        return request.user == view._get_news.author
