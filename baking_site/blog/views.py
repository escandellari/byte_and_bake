from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

# from .forms import PostForm
from .models import Post

# def post_detail(request, slug):
#     post = Post.objects.filter(slug=slug)
#     data = list(post.values())
#     print(data[0].get("content"))
#     # print(data.content)
#     return
#     # render(request, "blog/post_detail.html", {"post": data[0]})


def category_view(request, name):
    post_list = Post.objects.filter(category__name=name)

    return render(request, "blog/category.html", {"post_list": post_list, "category_name": name})
