from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Follow, Like

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Follow)