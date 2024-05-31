"""Serializers for the endpoints 'comments' to news of the 'Api' application v1."""

from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments."""

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author",
            "date_created_at",
        )
