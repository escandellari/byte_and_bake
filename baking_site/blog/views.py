from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogPost


class BlogPostView(ListView):
    model = BlogPost
    template_name = "blog/index.html"
