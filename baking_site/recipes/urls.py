from django.urls import path
from django.views.generic import DetailView

from .models import Post
from .views import AddRecipeView, DeleteRecipeView, EditRecipeView, category_view, recipes_view

urlpatterns = [
    path("", recipes_view, name="recipes"),
    path("add_recipe/", AddRecipeView.as_view(), name="add_recipe"),
    path("edit_recipe/<slug:slug>", EditRecipeView.as_view(), name="edit_recipe"),
    path("delete_recipe/<slug:slug>", DeleteRecipeView.as_view(), name="delete_recipe"),
    path("category/<str:name>", category_view, name="category"),
    path("<slug:slug>/", DetailView.as_view(model=Post), name="post_detail"),
]
