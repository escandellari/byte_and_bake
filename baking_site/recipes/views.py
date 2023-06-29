from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AddRecipeForm, EditRecipeForm
from .models import Post


class AddRecipeView(CreateView):
    model = Post
    form_class = AddRecipeForm
    template_name = "recipes/add_recipe.html"


class EditRecipeView(UpdateView):
    model = Post
    form_class = EditRecipeForm
    template_name = "recipes/edit_recipe.html"


class DeleteRecipeView(DeleteView):
    model = Post
    template_name = "recipes/delete_recipe.html"
    success_url = reverse_lazy("recipes")


def recipes_view(request):
    return render(request, "recipes/recipes.html")


def category_view(request, name):
    post_list = Post.objects.filter(category__name=name)
    return render(request, "recipes/category.html", {"post_list": post_list, "category_name": name})


def worldwide_view(request):
    return render(request, "recipes/worldwide.html")


def bread_view(request):
    return render(request, "recipes/bread.html")


def biscuits_view(request, name):
    post_list = Post.objects.filter(category__name=name)
    return render(request, "recipes/biscuits.html", {"post_list": post_list, "category_name": name})


def cakes_view(request):
    return render(request, "recipes/cakes.html")
