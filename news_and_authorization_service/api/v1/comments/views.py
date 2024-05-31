"""Views for the endpoints 'comments' to news of the 'Api' application v1."""

from django.shortcuts import get_object_or_404

from api.v1.comments.serializers import CommentSerializer
from api.v1.core.pagination import PageNumberPageSizePagination
from api.v1.core.permissions import IsUserAdmin, IsUserNewsAuthor, IsUserReadOnly
from api.v1.core.viewsets import GetPostDeleteViewSet
from news.models import News


class CommentsViewSet(GetPostDeleteViewSet):
    """URL requests handler to 'comments' to news resource endpoints"""

    name = "Comment to news resourse"
    description = "API endpoints to manage comments to news."

    serializer_class = CommentSerializer
    permission_classes = (IsUserReadOnly | IsUserNewsAuthor | IsUserAdmin,)
    pagination_class = PageNumberPageSizePagination
    ordering = ("-date_created_at",)

    @property
    def _get_news(self):
        print("get_news")
        return get_object_or_404(News, id=self.kwargs.get("news_id"))

    def get_queryset(self):
        return self._get_news.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, news=self._get_news)
