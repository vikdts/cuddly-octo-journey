from rest_framework import serializers
from .models import Comment
from django.contrib.contenttypes.models import ContentType

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    content_type = serializers.SlugRelatedField(queryset=ContentType.objects.all(), slug_field='model')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    object_id = serializers.IntegerField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 
            'content_type', 'object_id', 'created_at', 'updated_at', 'content'
        ]

class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')