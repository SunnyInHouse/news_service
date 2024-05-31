"""Serializers for the endpoints 'news' of the 'Api' application v1."""

from rest_framework import serializers

from comments.models import Comment
from news.models import News


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for read comments."""

    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author",
            "date_created_at",
        )


class NewsSerializer(serializers.ModelSerializer):
    """Serializer for work with news."""

    count_comments = serializers.IntegerField(
        source="_get_number_of_comments", read_only=True
    )
    count_likes = serializers.IntegerField(
        source="_get_number_of_likes", read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True, default=serializers.CurrentUserDefault()
    )
    comments_list = serializers.SerializerMethodField()

    def get_comments_list(self, obj):
        return CommentSerializer(
            obj.comments.select_related("author").all()[:10], many=True
        ).data

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author",
            "date_created_at",
            "date_updated_at",
            "count_comments",
            "count_likes",
            "comments_list",
        )
        read_only_fields = (
            "date_created_at",
            "date_updated_at",
        )
