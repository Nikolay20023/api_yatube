from rest_framework import viewsets, permissions


from posts.models import Group, Post
from api import serializers
from django.shortcuts import get_object_or_404


class IsOwnerOrReadOnly(permissions.BasePermission):
    """."""

    def has_object_permission(self, request, view, obj):
        """."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializers
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """."""

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializers


class CommentViewSet(viewsets.ModelViewSet):
    """."""

    serializer_class = serializers.CommentSerializers
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        """."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        """."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
