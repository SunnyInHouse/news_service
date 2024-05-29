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
            name="Like",
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
                    "author",
                    models.ForeignKey(
                        help_text="Author of the like",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="like_author",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="like author",
                    ),
                ),
                (
                    "news",
                    models.ForeignKey(
                        help_text="News to like",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="like_news",
                        to="news.news",
                        verbose_name="news to like",
                    ),
                ),
            ],
            options={
                "verbose_name": "like",
                "verbose_name_plural": "likes",
            },
        ),
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(
                fields=("author", "news"), name="unique_like_for_author_to_news"
            ),
        ),
    ]