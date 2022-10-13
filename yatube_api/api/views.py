from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from posts.models import Group, Post, Comment
from api import serializers
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    """."""

    serializer_class = serializers.PostSerializers

    def perform_create(self, serializer):
        """."""
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """."""
        pk = self.kwargs.get('pk')

        if not pk:
            return Post.objects.all()
        else:
            return Post.objects.filter(pk=pk)

    def perform_update(self, serializer):
        """."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено')
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        """."""
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено')
        return super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """."""

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializers


class CommentViewSet(viewsets.ModelViewSet):
    """."""

    serializer_class = serializers.CommentSerializers

    def get_queryset(self):
        """."""
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post=post_id)

    def perform_destroy(self, instance):
        """."""
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено')
        return super().perform_destroy(instance)

    def perform_update(self, serializer):
        """."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено')
        return super().perform_update(serializer)

    def perform_create(self, serializer):
        """."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post_id=post.id)
