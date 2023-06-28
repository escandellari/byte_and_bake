from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .models import Post


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
