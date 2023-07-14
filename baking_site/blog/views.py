from typing import Any, Dict

from django.contrib import messages
from django.http import HttpResponseRedirect
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

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse_lazy("blog_home")
            return HttpResponseRedirect(url)
        else:
            return super(EditPostView, self).post(request, *args, **kwargs)


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog_home")

    def post(self, request, *args, **kwargs):
        if not "cancel" in request.POST:
            return super(DeletePostView, self).post(request, *args, **kwargs)


def PreviewView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    messages.info(request, post.title, extra_tags="safe")
    messages.success(request, post.body, extra_tags="safe")
    return HttpResponseRedirect(reverse("blog_home"))
