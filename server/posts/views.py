from .serializers import PostSerializer, CommentSerializer
from .models import Post, PostImage, Comment
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            post = serializer.save(author=self.request.user)
            if "images" in self.request.FILES:
                uploaded_files = self.request.FILES.getlist('images')
                for uploaded_file in uploaded_files:
                    file_path = os.path.join("post_images/", uploaded_file.name)
                    default_storage.save(file_path, ContentFile(uploaded_file.read()))

                    # Сохраняем только имя файла в базе данных
                    PostImage.objects.create(post=post, file_name=uploaded_file.name)
        else:
            print(serializer.errors)


class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

    def get_object(self):
        post = super().get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        return post

    def perform_destroy(self, instance):
        # Удаляем все изображения, связанные с постом
        images = instance.images.all()  # Получаем связанные PostImage
        for image in images:
            file_path = os.path.join(settings.MEDIA_ROOT, "post_images", image.file_name)  # Формируем путь к файлу
            if os.path.exists(file_path):
                os.remove(file_path)  # Удаляем файл из хранилища

        # Теперь удаляем сам пост и записи о картинках в БД
        images.delete()  # Удаляем записи о картинках в БД
        instance.delete()  # Удаляем сам пост

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post = super().get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post.")
        return post

    def perform_update(self, serializer):
        post = serializer.save(author = self.request.user)
        if "images" in self.request.FILES:
            uploaded_files = self.request.FILES.getlist('images')
            for uploaded_file in uploaded_files:
                file_path = os.path.join("post_images/", uploaded_file.name)
                default_storage.save(file_path, ContentFile(uploaded_file.read()))

                # Сохраняем только имя файла в базе данных
                PostImage.objects.create(post=post, file_name=uploaded_file.name)

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]  # Publicly accessible

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Post.objects.filter(author_id=user_id).order_by("-created_at")


# 2️⃣ Get a specific post by its ID
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]  # Publicly accessible


# 3️⃣ Get any 20 posts (ignoring author)
class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]  # Publicly accessible

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")[:20]

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = generics.get_object_or_404(Post, id=post_id)
        serializer.save(user=self.request.user, post=post)

class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        comment = generics.get_object_or_404(Comment, id=self.kwargs["pk"])
        if comment.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit or delete this comment.")
        return comment

class PostCommentsListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post_id=post_id).order_by("-written_at")

