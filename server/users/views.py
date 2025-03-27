from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer, CustomTokenObtainPairSerializer


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    #
    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)

class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]  # Publicly accessible
    lookup_field = "user_id"

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")  # Get user_id from URL
        return Profile.objects.filter(user_id=user_id)  # Filter by user_id

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

