from django.urls import path
from . import views

urlpatterns = [
    path("/create", views.PostListCreateView.as_view(), name="post-list"),
    path("/delete/<int:pk>", views.PostDeleteView.as_view(), name="delete-post"),
    path("/update/<int:pk>", views.PostUpdateView.as_view(), name="update-post"),
    path("/user/<int:user_id>/", views.UserPostsView.as_view(), name="user-posts"),
    path("/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("", views.PostListView.as_view(), name="post-list"),
]