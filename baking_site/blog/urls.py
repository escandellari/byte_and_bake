from django.urls import include, path
from django.views.generic import DetailView

from .views import AddPostView, BlogHomeView, DeletePostView, EditPostView, PostDetailView, PreviewView

urlpatterns = [
    path("", BlogHomeView.as_view(), name="blog_home"),
    path("post_add/", AddPostView.as_view(), name="post_add"),
    path("post_edit/<slug:slug>", EditPostView.as_view(), name="post_edit"),
    path("post_delete/<slug:slug>", DeletePostView.as_view(), name="post_delete"),
    path("post_preview/<int:pk>", PreviewView, name="post_preview"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    # path("post_edit/<slug:slug>", EditRecipeView.as_view(), name="recipe_edit"),
]
