from django.contrib import admin
from .models import Post, Comment




class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'title', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'title', 'author', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
