"""Database settings of the 'News' application."""

from django.conf import settings
from django.db import models

from news.constants import FIELD_LIMITS_NEWS_APP


class News(models.Model):
    """Model News."""

    created_at = models.DateField(
        "news date created at",
        help_text="Date the news was created",
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
    )
    text = models.CharField(
        "news text",
        help_text="Text of the news",
        max_length=FIELD_LIMITS_NEWS_APP["text_max_char"],
        blank=True,
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
        ordering = ("-created_at",)

    def __str__(self):
        return f"News {self.title}, Author {self.author}."
