"""Admin site settings of the 'Comments' application."""

from django.contrib import admin

from comments.models import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """Settings for presenting 'News' model on the admin site."""

    list_display = (
        "id",
        "news",
        "author",
        "date_created_at",
    )
    list_select_related = True
    search_fields = (
        "news__title",
        "author__username",
        "date_created_at",
    )
    readonly_fields = ("date_created_at",)
    fields = (
        "news",
        "author",
        "text",
        "date_created_at",
    )
