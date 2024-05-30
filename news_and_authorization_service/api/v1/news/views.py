"""Views for 'news' endpoints of the 'Api' application v1."""

from api.v1.core.viewsets import GetPostPutDeleteViewSet


class NewsViewSet(GetPostPutDeleteViewSet):
    """URL requests handler to 'News' resource endpoints"""

    name = "News resourse"
    description = "API endpoints to manage news."
