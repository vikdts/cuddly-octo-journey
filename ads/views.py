from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Ad
from .serializers import AdSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.
class AdList(generics.ListCreateAPIView):
    serializer_class = AdSerializer