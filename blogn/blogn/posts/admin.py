from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'author', 'mod_date']
    search_fields = ['id', 'title', 'excerpt', 'body', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)
