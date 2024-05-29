"""Admin site settings of the 'News' application."""

from django.contrib import admin

from news.models import News


@admin.register(News)
class CourseAdmin(admin.ModelAdmin):
    """Settings for presenting 'News' model on the admin site."""

    list_display = (
        "id",
        "title",
        "author",
        "created_at",
    )
    list_select_related = True
    search_fields = ("title", "author", "created_at")
    eadonly_fields = ("created_at",)
    fields = (
        "title",
        "author",
        "text",
    )
