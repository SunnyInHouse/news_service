"""Database settings of the 'News' application."""

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from news.constants import FIELD_LIMITS_NEWS_APP, FIELD_REGEXES_NEWS_APP


class News(models.Model):
    """Model News."""

    date_created_at = models.DateTimeField(
        "news date created at",
        help_text="Date the news was created",
        auto_now_add=True,
    )
    date_updated_at = models.DateTimeField(
        "news date updated at",
        help_text="Date the news was updated",
        auto_now_add=True,
    )
    title = models.CharField(
        "news title",
        help_text="News name",
        max_length=FIELD_LIMITS_NEWS_APP["title_max_char"],
        unique=True,
        error_messages={
            "unique": "A news with this name already exists.",
        },
        validators=(RegexValidator(FIELD_REGEXES_NEWS_APP["title"]),),
    )
    text = models.TextField(
        "news text",
        help_text="Text of the news",
        max_length=FIELD_LIMITS_NEWS_APP["text_max_char"],
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="news author",
        help_text="Author of the news",
        on_delete=models.PROTECT,
        related_name="news_author",
    )

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"
        ordering = ("-date_updated_at",)

    def __str__(self):
        return f"News {self.title}, Author {self.author}."

    def _get_number_of_comments(self):
        """Calculate count of comments to news."""
        return self.comments.count()

    _get_number_of_comments.short_description = "count of comments to news"

    def _get_number_of_likes(self):
        """Calculate count of likes to news."""
        return self.likes.count()

    _get_number_of_likes.short_description = "count of likes to news"
