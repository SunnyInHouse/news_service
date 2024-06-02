"""Admin site settings of the 'Users' application."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from comments.models import Comment
from likes.models import Like
from news.models import News
from users.models import User


class CommentsInLine(admin.TabularInline):
    """Settings for presenting 'Comment' model in 'News' model on the admin site."""

    model = Comment
    extra = 1
    max_num = 5


class LikestInLine(admin.TabularInline):
    """Settings for presenting 'Like' model in 'News' model on the admin site."""

    model = Like
    extra = 1
    max_num = 5


class NewsInLine(admin.TabularInline):
    """Settings for presenting 'Like' model in 'News' model on the admin site."""

    model = News
    extra = 1
    max_num = 5


@admin.register(User)
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
    inlines = (
        NewsInLine,
        CommentsInLine,
        LikestInLine,
    )
