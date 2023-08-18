from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Category, Post


# Create your tests here.
class CategoryModelTest(TestCase):
    def create_category(self):
        return Category.objects.create(category_name="Category test")

    def test_category_creation(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), str(category))

    # def test_absolute_url(self):
    #     category = self.create_category()
    #     self.assertEqual(category.get_absolute_url(), "")


class PostModelTest(TestCase):
    def create_post(self):
        title = "Title test"
        author = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        return Post.objects.create(title=title, author=author)

    def test_blog_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title + " | " + str(post.author))

    def test_absolute_url(self):
        post = self.create_post()
        self.assertEqual(post.get_absolute_url(), "/blog/")
