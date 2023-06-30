from django.urls import path
from django.views.generic import DetailView

from .models import Post
from .views import (
    AddRecipeView,
    DeleteRecipeView,
    EditRecipeView,
    biscuits_view,
    bread_view,
    cakes_view,
    category_view,
    recipes_view,
    worldwide_view,
)

urlpatterns = [
    # path("", views.PostList.as_view(), name="post_list"),
    # path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("", recipes_view, name="recipes"),
    path("category/<str:name>", category_view, name="category"),
    path("<slug:slug>/", DetailView.as_view(model=Post), name="post_detail"),
    path("add_recipe/", AddRecipeView.as_view(), name="add_recipe"),
    path("edit_recipe/<slug:slug>", EditRecipeView.as_view(), name="edit_recipe"),
    path("delete_recipe/<slug:slug>", DeleteRecipeView.as_view(), name="delete_recipe"),
]
