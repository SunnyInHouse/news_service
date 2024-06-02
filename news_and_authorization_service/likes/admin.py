"""Admin site settings of the 'Likes' application."""

from django.contrib import admin

from likes.models import Like


@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
    """Settings for presenting 'Likes' model on the admin site."""

    list_display = (
        "id",
        "news",
        "author",
    )
    list_select_related = True
    search_fields = (
        "news__title",
        "author__username",
    )
    fields = (
        "news",
        "author",
    )
