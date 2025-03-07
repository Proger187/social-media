from django.urls import path
from . import views

urlpatterns = [
    path("/post/<int:post_id>/create", views.PostLikeCreateView.as_view(), name="like-post"),
    path("/post/delete/<int:pk>", views.PostLikeRemove.as_view(), name="delete-post-like"),
    path("/comment/<int:comment_id>/create", views.CommentLikeCreateView.as_view(), name="like-comment"),
    path("/comment/delete/<int:pk>/", views.CommentLikeRemove.as_view(), name="delete-comment-like"),
    path("/subscribe/<int:subscribed_to_id>", views.SubscribeCreateView.as_view(), name="subscribe"),
    path("/subscribe/delete/<int:pk>", views.SubscribeRemoveView.as_view(), name="remove-subscribe"),
]