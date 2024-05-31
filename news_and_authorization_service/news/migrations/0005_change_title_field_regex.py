# Generated by Django 5.0.6 on 2024-05-31 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_change_text_field_length_and_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                error_messages={"unique": "A news with this name already exists."},
                help_text="News name",
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[a-zA-Zа-яА-ЯёЁ0-9.!?,_()\\\"<>»«'%:; \\-]+$"
                    )
                ],
                verbose_name="news title",
            ),
        ),
    ]