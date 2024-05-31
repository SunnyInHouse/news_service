"""Views for endpoints 'news' of the 'Api' application v1."""

from api.v1.core.pagination import PageNumberPageSizePagination
from api.v1.core.permissions import IsUserAdmin, IsUserOwner, IsUserReadOnly
from api.v1.news.serializers import NewsSerializer
from api.v1.core.viewsets import GetPostPutDeleteViewSet
from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from news.models import News


@activate_drf_spectacular_view_decorator
class NewsViewSet(GetPostPutDeleteViewSet):
    """URL requests handler to 'News' resource endpoints"""

    name = "News resourse"
    description = "API endpoints to manage news."

    queryset = News.objects.select_related("author").prefetch_related("comments")
    serializer_class = NewsSerializer
    permission_classes = (IsUserReadOnly | IsUserOwner | IsUserAdmin,)
    lookup_field = "id"
    pagination_class = PageNumberPageSizePagination
    ordering = ("-date_updated_at",)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
