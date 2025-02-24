from django.urls import path
from . import views

urlpatterns = [
    path("/create", views.PostListCreateView.as_view(), name="post-list"),
    path("/delete/<int:pk>", views.PostDeleteView.as_view(), name="delete-post"),
    path("/update/<int:pk>", views.PostUpdateView.as_view(), name="update-post"),
    path("/user/<int:user_id>/", views.UserPostsView.as_view(), name="user-posts"),
    path("/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("", views.PostListView.as_view(), name="post-list"),
    path("/<int:post_id>/comments/", views.PostCommentsListView.as_view(), name="post-comments"),
    path("/<int:post_id>/comments/create/", views.CommentCreateView.as_view(), name="create-comment"),
    path("/comments/<int:pk>/", views.CommentUpdateDeleteView.as_view(), name="update-delete-comment"),
]