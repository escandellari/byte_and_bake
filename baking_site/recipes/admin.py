from django.contrib import admin

from .models import Category, Comment, Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "snippet",
        "slug",
        "author",
        "date_published",
    )
    search_fields = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "recipe", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
