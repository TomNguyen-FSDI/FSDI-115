from django.contrib import admin
from .models import Post, Comment, Community, Follow_community, InboxMessage

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

admin.site.register(Community)
admin.site.register(Follow_community)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(InboxMessage)
