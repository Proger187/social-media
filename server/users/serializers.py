from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'birth_date', 'avatar']
        read_only_fields = ["user"]

    def update(self, instance, validated_data):
        # Prevent changing the user field
        validated_data.pop("user", None)
        return super().update(instance, validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom fields to the token
        token["username"] = user.username
        token["email"] = user.email
        token["birth_date"] = user.profile.birth_date
        token["bio"] = user.profile.bio
        if user.profile.avatar and hasattr(user.profile.avatar, "url"):
            token["avatar"] = user.profile.avatar.url
        else:
            token["avatar"] = None

        return token

