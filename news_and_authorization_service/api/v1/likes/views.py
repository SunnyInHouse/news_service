"""Views for the endpoints 'likes' to news of the 'Api' application v1."""

from django.shortcuts import get_object_or_404

from api.v1.likes.serializers import LikeSerializer
from api.v1.core.pagination import PageNumberPageSizePagination
from api.v1.core.permissions import IsUserAdmin, IsUserNewsAuthor, IsUserReadOnly
from api.v1.core.viewsets import GetPostDeleteViewSet
from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from news.models import News


@activate_drf_spectacular_view_decorator
class LikesViewSet(GetPostDeleteViewSet):
    """URL requests handler to 'likess' to news resource endpoints"""

    name = "Like to news resourse"
    description = "API endpoints to manage likes to news."

    serializer_class = LikeSerializer
    permission_classes = (IsUserReadOnly | IsUserNewsAuthor | IsUserAdmin,)
    lookup_field = "id"
    pagination_class = PageNumberPageSizePagination
    ordering = ("-date_created_at",)

    @property
    def _get_news(self):
        return get_object_or_404(News, id=self.kwargs.get("news_id"))

    def get_queryset(self):
        return self._get_news.likes.select_related("author", "news").all()

    def get_serializer_context(self):
        serializer_context = super().get_serializer_context()
        if self.request.method == "POST":
            serializer_context.update(news=self._get_news)
        return serializer_context

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, news=self._get_news)
