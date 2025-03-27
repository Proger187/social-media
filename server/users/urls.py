from tkinter.font import names
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserView, ProfileView, ProfileDetailView, CustomTokenObtainPairView

urlpatterns = [
    path('/register', CreateUserView.as_view(), name="register"),
    path("/token", CustomTokenObtainPairView.as_view(), name="get_token"),
    path("/token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("/profile", ProfileView.as_view(), name="profile"),
    path('/profile/<int:user_id>', ProfileDetailView.as_view(), name="profile-details")
]