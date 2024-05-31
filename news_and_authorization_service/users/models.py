"""Database settings of the 'Users' application."""

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.constants import FIELD_LIMITS_USERS_APP, FIELD_REGEXES_USERS_APP
from users.manager import UserManager
from users.validators import validate_username_not_me


class User(AbstractUser):
    """Modified model User."""

    username = models.CharField(
        "username",
        help_text="User's username",
        max_length=FIELD_LIMITS_USERS_APP["username_max_char"],
        unique=True,
        error_messages={"unique": "A user with that username already exists."},
        validators=(
            RegexValidator(FIELD_REGEXES_USERS_APP["username"]),
            validate_username_not_me,
        ),
    )
    password = models.CharField(
        "password",
        help_text="User's password",
        max_length=FIELD_LIMITS_USERS_APP["password_max_char"],
    )
    is_superuser = models.BooleanField(
        "admin status",
        help_text="Designates whether the user can log into this admin site.",
        default=False,
    )

    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("username",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.is_superuser

    @property
    def is_user(self):
        return not self.is_superuser
