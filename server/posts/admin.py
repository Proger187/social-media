from django.contrib import admin
from .models import Post, PostImage, Comment
from django.utils.html import format_html
from django.contrib.auth.models import User

# Register your models here.

class PostImageInline(admin.TabularInline):  # Use StackedInline if you prefer a different UI
    model = PostImage
    extra = 1  # Number of empty image fields to show by default
    fields = ("file_name", "image_preview")  # Display relevant fields
    readonly_fields = ("image_preview",)  # Make image preview read-only

    def image_preview(self, obj):
        if obj.file_name:  # Assuming 'file_name' is an ImageField
            return format_html(
                f'<img src="/media/post_images/{obj.file_name}" width="100" height="100" style="object-fit: cover;"/>')
        return "No Image"

    image_preview.short_description = "Preview"  # Column name in admin

class CommentAdmin(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")  # Show main post info
    list_editable = ("title",)  # Editable fields in list view
    search_fields = ("title", "content")  # Enable search
    list_filter = ("created_at", "author")  # Filters in admin panel
    inlines = [PostImageInline, CommentAdmin]  # Attach images inline to PostAdmin


admin.site.register(Post, PostAdmin)

