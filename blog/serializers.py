from rest_framework import serializers
from .models import Post


class PostThumbnailSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'nickname', 'title','date']

class PostDetailSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'nickname', 'body', 'title','date']