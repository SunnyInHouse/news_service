"""Admin site settings of the 'News' application."""

from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Settings for presenting 'News' model on the admin site."""

    list_display = (
        "id",
        "title",
        "author",
        "date_created_at",
        "_get_number_of_comments",
        "_get_number_of_likes",
    )
    list_select_related = True
    search_fields = (
        "title",
        "author__username",
        "date_created_at",
        "date_updated_at",
    )
    readonly_fields = (
        "date_created_at",
        "date_updated_at",
    )
    fields = (
        "title",
        "author",
        "text",
        "date_created_at",
        "date_updated_at",
    )
