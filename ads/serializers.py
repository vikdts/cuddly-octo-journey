from .models import Ad
from rest_framework import serializers

class AdoptSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')