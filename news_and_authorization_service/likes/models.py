"""Database settings of the 'Likes' application."""

from django.conf import settings
from django.db import models

from news.models import News


class Like(models.Model):
    """Model Likes."""

    news = models.ForeignKey(
        News,
        verbose_name="news to like",
        help_text="News to like",
        on_delete=models.CASCADE,
        related_name="like_news",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="like author",
        help_text="Author of the like",
        on_delete=models.CASCADE,
        related_name="like_author",
    )

    class Meta:
        verbose_name = "like"
        verbose_name_plural = "likes"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "author",
                    "news",
                ),
                name="unique_like_for_author_to_news",
            ),
        )
