from django.contrib import admin

from .models import Category, Recipe


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


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
