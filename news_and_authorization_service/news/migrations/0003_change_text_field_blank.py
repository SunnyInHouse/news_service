# Generated by Django 5.0.6 on 2024-05-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_edit_regex_for_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="text",
            field=models.CharField(
                help_text="Text of the news", max_length=1500, verbose_name="news text"
            ),
        ),
    ]