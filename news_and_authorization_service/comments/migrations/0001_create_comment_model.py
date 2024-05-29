# Generated by Django 5.0.6 on 2024-05-29 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("news", "0001_create_news_model"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date the comments was created",
                        verbose_name="comments date created at",
                    ),
                ),
                (
                    "text",
                    models.CharField(
                        help_text="Text of the news",
                        max_length=500,
                        verbose_name="news text",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="Author of the news",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_author",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="news author",
                    ),
                ),
                (
                    "news",
                    models.ForeignKey(
                        help_text="Comment for this news",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_news",
                        to="news.news",
                        verbose_name="comment for news",
                    ),
                ),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "comments",
                "ordering": ("-date_created_at",),
            },
        ),
        migrations.AddConstraint(
            model_name="comment",
            constraint=models.UniqueConstraint(
                fields=("author", "news"), name="unique_comment_for_author_to_news"
            ),
        ),
    ]