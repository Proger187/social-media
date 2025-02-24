from rest_framework import serializers
from .models import Post, PostImage, Comment


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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "user", "post", "written_at"]
        extra_kwargs = {"user": {"read_only": True}, "post": {"read_only": True}}