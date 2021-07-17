from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (
    Post, Comment, Community, Follow_community, InboxMessage, Profile
    )

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Community)
admin.site.register(Follow_community)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(InboxMessage)
admin.site.register(Profile)
