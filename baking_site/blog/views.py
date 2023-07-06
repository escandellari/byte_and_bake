from typing import Any, Dict

from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import EditForm, PostForm
from .models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-id"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_add.html"


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/post_edit.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog_home")
