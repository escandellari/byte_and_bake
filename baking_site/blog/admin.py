from django.contrib import admin

from .models import Category, Post


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "title_tag",
        "slug",
        "author",
        "date_published",
    )
    search_fields = ["title", "body", "author"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, BlogPostAdmin)
admin.site.register(Category)
