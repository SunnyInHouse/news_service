"""Constants for models of 'Users' application."""

FIELD_LIMITS_USERS_APP = {
    "password_max_char": 128,
    "username_max_char": 150,
}

FIELD_REGEXES_USERS_APP = {
    "username": r"^[a-zA-Z0-9_\-]+$",
}

STRING_CONSTANTS_USERS_APP = {
    "unacceptable_username": "me",
}
