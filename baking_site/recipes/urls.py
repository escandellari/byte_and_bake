from django.urls import path
from django.views.generic import DetailView

from .models import Recipe
from .views import AddCategoryView, DeleteRecipeView, EditRecipeView, category_view, recipe_add_view, recipes_view

urlpatterns = [
    path("", recipes_view, name="recipes"),
    path("category/<str:name>", category_view, name="category"),
    path("category_add/", AddCategoryView.as_view(), name="category_add"),
    path("recipe_add/", recipe_add_view, name="recipe_add"),
    path("recipe_edit/<slug:slug>", EditRecipeView.as_view(), name="recipe_edit"),
    path("recipe_delete/<slug:slug>", DeleteRecipeView.as_view(), name="recipe_delete"),
    path("<slug:slug>/", DetailView.as_view(model=Recipe), name="recipe_detail"),
]
