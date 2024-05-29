"""Defining a manager for models of 'Users' application."""

from typing import Any

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Modified standard user manager."""

    def create_user(
        self,
        username: str,
        password: str | None,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> Any:
        """Create a user."""
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.is_active = True
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, username: str, password: str | None) -> Any:
        """Create a superuser."""
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save(using=self._db)
        return user
