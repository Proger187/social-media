from django.urls import path
from . import views

urlpatterns = [
    path("/post/<int:post_id>/create", views.PostLikeCreateView.as_view(), name="like-post"),
    path("/post/delete/<int:pk>", views.PostLikeRemove.as_view(), name="delete-post-like"),
    path("/post/<int:post_id>/", views.PostGetLikes.as_view(), name="get-post-likes"),
    path("/comment/<int:comment_id>/create", views.CommentLikeCreateView.as_view(), name="like-comment"),
    path("/comment/delete/<int:pk>", views.CommentLikeRemove.as_view(), name="delete-comment-like"),
    path("/comment/<int:comment_id>/", views.CommentGetLikes.as_view(), name="get-comment-likes"),
    path("/subscribe/<int:subscribed_to_id>/create", views.SubscribeCreateView.as_view(), name="subscribe"),
    path("/subscribe/delete/<int:pk>", views.SubscribeRemoveView.as_view(), name="remove-subscribe"),
    path("/subscribe/<int:subscribed_to_id>/", views.GetSubscribers.as_view(), name="get-user-subscribers")
]