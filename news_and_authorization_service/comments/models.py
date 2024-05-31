"""Database settings of the 'Comments' application."""

from django.conf import settings
from django.db import models

from comments.constants import FIELD_LIMITS_COMMENTS_APP
from news.models import News


class Comment(models.Model):
    """Model Comments."""

    date_created_at = models.DateTimeField(
        "comments date created at",
        help_text="Date the comments was created",
        auto_now_add=True,
    )
    text = models.TextField(
        "comment text",
        help_text="Text of the comment",
        max_length=FIELD_LIMITS_COMMENTS_APP["text_max_char"],
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="comment author",
        help_text="Author of the comment",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    news = models.ForeignKey(
        News,
        verbose_name="comment for news",
        help_text="Comment for this news",
        on_delete=models.CASCADE,
        related_name="comments",
    )

    class Meta:
        ordering = ("-date_created_at",)
        verbose_name = "comment"
        verbose_name_plural = "comments"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "author",
                    "text",
                    "news",
                ),
                name="unique_comment_for_author_to_news",
            ),
        )

    def __str__(self):
        return f"Comment to {self.news}, Author {self.author}."
