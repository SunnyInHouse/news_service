"""Serializers for the endpoints 'likes' to news of the 'Api' application v1."""

from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for likes."""

    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    news = serializers.StringRelatedField(read_only=True)

    default_error_messages = {
        "like_is_exists": "You already liked this news.",
    }

    class Meta:
        model = Like
        fields = (
            "id",
            "author",
            "news",
            "date_created_at",
        )

    def validate(self, attrs):
        if Like.objects.filter(
            author=self.context.get("request").user, news=self.context.get("news")
        ).exists():
            raise serializers.ValidationError(
                {"detail": self.error_messages["like_is_exists"]}
            )
        return super().validate(attrs)
