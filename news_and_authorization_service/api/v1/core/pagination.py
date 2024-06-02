"""Paginators for the 'Api' application v1."""

from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.v1.core.constants import PAGINATION_LIMITS, PAGINATION_PARAMS


class PageNumberPageSizePagination(PageNumberPagination):
    """Pagination class that supports page numbers and page size as query parameters."""

    page_size = PAGINATION_LIMITS["page_size"]
    page_query_param = PAGINATION_PARAMS["page"]
    page_size_query_param = PAGINATION_PARAMS["page_size"]
    max_page_size = PAGINATION_LIMITS["max_page_size"]

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count_on_pages", self.page.paginator.count),
                    ("total_pages", self.page.paginator.num_pages),
                    ("next_page", self.get_next_link()),
                    ("previous_page", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 123,
                },
                "total_pages": {
                    "type": "integer",
                    "example": 12,
                },
                "next_page": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?{page_query_param}=4".format(
                        page_query_param=self.page_query_param
                    ),
                },
                "previous_page": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?{page_query_param}=2".format(
                        page_query_param=self.page_query_param
                    ),
                },
                "results": schema,
            },
        }
