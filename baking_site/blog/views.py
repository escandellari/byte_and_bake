from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .models import Post


def category_view(request, name):
    post_list = Post.objects.filter(category__name=name)
    return render(request, "blog/category.html", {"post_list": post_list, "category_name": name})


def worldwide_view(request):
    return render(request, "blog/worldwide.html")


def recipes_view(request):
    return render(request, "blog/recipes.html")
