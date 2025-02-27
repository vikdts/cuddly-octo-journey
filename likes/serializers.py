from rest_framework import serializers
from likes.models import Like
from django.db import IntegrityError
from django.contrib.contenttypes.models import ContentType

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    content_type = serializers.SlugRelatedField(slug_field="model", queryset=ContentType.objects.all())
    object_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['id', 'owner', 'created_at', 'content_type', 'object_id']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })