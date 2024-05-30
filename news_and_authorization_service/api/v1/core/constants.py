"""Constants of the 'Api' application v1."""

import os

from dotenv import load_dotenv

load_dotenv()

PAGINATION_LIMITS = {
    "page_size": int(os.getenv("PAGINATION_PAGE_SIZE", 5)),
    "max_page_size": int(os.getenv("PAGINATION_MAX_PAGE_SIZE", 30)),
}

PAGINATION_PARAMS = {
    "page": "page",
    "page_size": "page_size",
}
