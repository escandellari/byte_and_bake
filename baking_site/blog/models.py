from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.urls import reverse


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=150)
    date_published = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog_home")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self.slugify(self.title)
        return super(BlogPost, self).save(*args, **kwargs)

    def slugify(self, tag):
        slug = default_slugify(tag)
        return slug
