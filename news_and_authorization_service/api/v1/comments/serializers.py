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
    news = serializers.StringRelatedField(read_only=True)

    default_error_messages = {
        "comment_is_exists": "You already comment this news with this text.",
    }

    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author",
            "news",
            "date_created_at",
        )

    def validate(self, attrs):
        if Comment.objects.filter(
            author=self.context.get("request").user,
            news=self.context.get("news"),
            text=attrs["text"],
        ).exists():
            raise serializers.ValidationError(
                {"detail": self.error_messages["comment_is_exists"]}
            )
        return super().validate(attrs)
