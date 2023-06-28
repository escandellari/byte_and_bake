from django.urls import path
from django.views.generic import DetailView

from .models import Post
from .views import category_view, recipes_view, worldwide_view

urlpatterns = [
    # path("", views.PostList.as_view(), name="post_list"),
    # path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("<slug:slug>/", DetailView.as_view(model=Post), name="post_detail"),
    path("category/<str:name>", category_view, name="category"),
    path("recipes", recipes_view, name="recipes"),
    path("worldwide", worldwide_view, name="worldwide"),
]
