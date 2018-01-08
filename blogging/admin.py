from django.contrib import admin

from blogging.models import Post

class PostAdminModel(admin.ModelAdmin):
    list_filter = ['title', 'updated']
    list_display = ['title','content','updated']
    search_fields = ['title','content']
    class Meta:
        model=Post
admin.site.register(Post,PostAdminModel)
