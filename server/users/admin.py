from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ["birth_date", "bio", "verified"]
    list_display = ["user", "birth_date", "bio", "verified"]

admin.site.register(Profile, ProfileAdmin)