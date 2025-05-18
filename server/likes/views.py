from .serializers import PostLikeSerializer, CommentLikeSerializer, SubscribeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from posts.models import Post, Comment
from .models import Subscribe, PostLike, CommentLike
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User

# Create your views here.
class PostLikeCreateView(generics.CreateAPIView):
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = generics.get_object_or_404(Post, id=post_id)
        serializer.save(user=self.request.user, post=post)

class PostLikeRemove(generics.DestroyAPIView):
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()
    permission_classes = [IsAuthenticated]

class PostGetLikes(generics.ListAPIView):
    serializer_class = PostLikeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return PostLike.objects.filter(post=post_id).select_related("user")

class CommentLikeCreateView(generics.CreateAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        comment_id = self.kwargs.get("comment_id")
        comment = generics.get_object_or_404(Comment, id=comment_id)
        serializer.save(user=self.request.user, comment=comment)

class CommentLikeRemove(generics.DestroyAPIView):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()
    permission_classes = [IsAuthenticated]

class CommentGetLikes(generics.ListAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        comment_id = self.kwargs.get("comment_id")
        return CommentLike.objects.filter(comment=comment_id).select_related("user")

class SubscribeCreateView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        subscribed_to_id = self.kwargs.get("subscribed_to_id")
        serializer.save(subscriber=self.request.user, subscribed_to_id=subscribed_to_id)

class SubscribeRemoveView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsAuthenticated]

class GetSubscribers(generics.ListAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        subscribed_to_id = self.kwargs.get("subscribed_to_id")
        return Subscribe.objects.filter(subscribed_to=subscribed_to_id)



