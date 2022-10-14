from email.policy import default
from rest_framework import serializers
from posts.models import Post, Comment, Group


class CommentSerializers(serializers.ModelSerializer):
    """."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """."""

        model = Comment
        fields = ('author', 'post', 'text', 'created', 'id')


class PostSerializers(serializers.ModelSerializer):
    """."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """."""

        model = Post
        fields = (
            'text', 'pub_date', 'author', 'image', 'group', 'id'
        )


class GroupSerializers(serializers.ModelSerializer):
    """."""

    class Meta:
        """."""

        model = Group
        fields = ('title', 'slug', 'description')
