from django.contrib import admin

from .models import Category, Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "created_on",
        "prep_time",
    )
    search_fields = ["title", "content", "serves"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
