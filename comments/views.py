from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from django.contrib.contenttypes.models import ContentType

# Create your views here.
class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(self.get_object())
        object_id = self.get_object().id
        serializer.save(owner=self.request.user, content_type=content_type, object_id=object_id)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()