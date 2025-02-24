from rest_framework import serializers
from .models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "file_name", "uploaded_at"]


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "author", "images"]
        extra_kwargs = {"author": {"read_only": True}}

