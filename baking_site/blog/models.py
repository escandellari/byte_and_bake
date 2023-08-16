from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.urls import reverse
from tinymce.models import HTMLField


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)

    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=255, default="baking")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = HTMLField(blank=True, null=True)
    snippet = models.CharField(max_length=150)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog_home")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self.slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def slugify(self, tag):
        slug = default_slugify(tag)
        return slug
