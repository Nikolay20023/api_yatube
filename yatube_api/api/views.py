from rest_framework import viewsets
from posts.models import Group, Post, Comment
from .serializers import *
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializers


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializers

    def get_queryset(self):
        post_id = self.kwargs.get("pk")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset


    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        serializer.save(author=self.request.user, post=post)
