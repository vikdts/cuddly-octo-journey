from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Ad
from .serializers import AdSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.
class AdList(generics.ListCreateAPIView):
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ad.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdSerializer
    queryset = Ad.objects.all()