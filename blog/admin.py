from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("likes", "tags")


class TagAdmin(admin.ModelAdmin):
    raw_id_fields = ("posts",)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ("post",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
