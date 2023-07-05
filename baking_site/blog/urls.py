from django.urls import include, path

from .views import BlogPostView

urlpatterns = [
    path("", BlogPostView.as_view(), name="blog_home"),
]
