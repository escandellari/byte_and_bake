from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..forms import PostForm
from ..models import Post


class TestForms(TestCase):
    def setUp(self):
        self.author = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    def test_valid_form(self):
        post = Post.objects.create(
            title="title",
            title_tag="title_tag",
            category="category",
            author=self.author,
            body="body",
            snippet="snippet",
        )
        data = {
            "title": post.title,
            "title_tag": post.title_tag,
            "author": post.author,
            "body": post.body,
            "category": post.category,
            "snippet": post.snippet,
        }

        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        post = Post.objects.create(
            title="title", title_tag="title_tag", category="category", author=self.author, body="body", snippet=""
        )
        data = {
            "title": post.title,
            "title_tag": post.title_tag,
            "author": post.author,
            "body": post.body,
            "category": post.category,
            "snippet": post.snippet,
        }

        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
