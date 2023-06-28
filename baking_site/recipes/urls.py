from django.urls import path
from django.views.generic import DetailView

from .models import Post
from .views import biscuits_view, bread_view, cakes_view, category_view, recipes_view, worldwide_view

urlpatterns = [
    # path("", views.PostList.as_view(), name="post_list"),
    # path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("", recipes_view, name="recipes"),
    path("biscuits/<str:name>", biscuits_view, name="biscuits"),
    path("<slug:slug>/", DetailView.as_view(model=Post), name="post_detail"),
    path("category/<str:name>", category_view, name="category"),
    path("worldwide", worldwide_view, name="worldwide"),
    path("bread", bread_view, name="bread"),
    path("cakes", cakes_view, name="cakes"),
]
