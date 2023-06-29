from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=150, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + " | " + str(self.author)

    @property
    def post_images(self):
        return self.postimage_set.all()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self.slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def slugify(self, tag):
        slug = default_slugify(tag)
        return slug


class PostImage(models.Model):
    image = models.ImageField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.image)


class Category(models.Model):
    name = models.CharField(max_length=255)
    post = models.ManyToManyField("Post")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
