from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.urls import reverse
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_list")


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    snippet = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    category = models.ManyToManyField("Category", related_name="recipes")

    image = models.ImageField(null=True, blank=True, upload_to="images/")

    prep_time = models.CharField(max_length=200, blank=True, null=True)
    cook_time = models.CharField(max_length=200, blank=True, null=True)
    proof_time = models.CharField(max_length=200, blank=True, null=True)
    serves = models.CharField(max_length=200, blank=True, null=True)

    ingredients = HTMLField(blank=True, null=True)
    method = HTMLField(blank=True, null=True)
    story_time = HTMLField(blank=True, null=True, default="")

    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.title + " | " + str(self.author)

    @property
    def post_images(self):
        return self.postimage_set.all()

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self.slugify(self.title)
        return super(Recipe, self).save(*args, **kwargs)

    def slugify(self, tag):
        slug = default_slugify(tag)
        return slug
