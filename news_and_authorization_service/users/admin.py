"""Admin site settings of the 'Users' application."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.models import Users


@admin.register(Users)
class UsersAdmin(DjangoUserAdmin):
    """Settings for presenting 'User' model on the admin site."""

    list_display = (
        "id",
        "username",
        "is_superuser",
    )
    search_fields = ("username",)
    readonly_fields = ("date_joined",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_superuser",),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_superuser",
                ),
            },
        ),
    )
