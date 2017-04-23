from django.contrib import admin
from .models import Post
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'author', 'mod_date']
    search_fields = ['id', 'title', 'excerpt', 'body', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_date', 'author', 'body']
    search_fields = ['id', 'body', 'author__username']
    # prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Comment, CommentAdmin)
