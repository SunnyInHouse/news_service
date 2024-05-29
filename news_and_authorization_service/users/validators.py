"""A module containing validators for users model fields."""

from django.core.exceptions import ValidationError

from users.constants import STRING_CONSTANTS_USERS_APP


def validate_username_not_me(value: str) -> None:
    """Check username != UNACCEPTABLE_USERNAME."""
    if value.lower() == STRING_CONSTANTS_USERS_APP["unacceptable_username"]:
        raise ValidationError(
            "The name '{value}' is not allowed.".format(value=value),
        )
