from rest_framework import serializers
from likes.models import Like
from posts.models import Post
from ads.models import Ad
from django.db import IntegrityError

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post', 'ad', 'liked']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
