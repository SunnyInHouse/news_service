"""Constants for models of 'News' application."""

FIELD_LIMITS_NEWS_APP = {
    "title_max_char": 150,
    "text_max_char": 1500,
}

FIELD_REGEXES_NEWS_APP = {
    "title": r"^[a-zA-Zа-яА-ЯёЁ0-9.!?,_ \-]+$",
}
