from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'nickname', 'title', 'body','date']