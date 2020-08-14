from django.contrib import admin
from .models import Post, Comment, Category, Popular_Article

admin.site.site_header = "Moi's Blog Admin Dashboard"


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category_tags',
                    'view_count', 'published_date']
    list_filter = ['published_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_date', 'reply']
    list_filter = ['created_date']


class PopularPostAdmin(admin.ModelAdmin):
    list_display = ['popular_post', 'date_added']
    list_filter = ['date_added']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Popular_Article, PopularPostAdmin)
