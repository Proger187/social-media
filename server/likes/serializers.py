from math import trunc

from rest_framework import serializers, viewsets, permissions
from django.contrib.auth.models import User
from .models import PostLike, CommentLike, Subscribe
from users.serializers import UserSerializer


class PostLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PostLike
        fields = ["id", "post", "user"]
        extra_kwargs = {"user": {"read_only": True}, "post": {"read_only": True}}


class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = CommentLike
        fields = ["id", "comment", "user"]
        extra_kwargs = {"user": {"read_only": True}, "comment": {"read_only": True}}


class SubscribeSerializer(serializers.ModelSerializer):
    subscriber = UserSerializer(read_only=True)
    class Meta:
        model = Subscribe
        fields = ["id", "subscriber", "subscribed_to"]
        extra_kwargs = {"subscriber": {"read_only": True}, "subscribed_to": {"read_only": True}}
