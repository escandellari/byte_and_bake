from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.urls import reverse


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

    image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=150, blank=True, null=True, default="uncategorised")

    prep_time = models.CharField(max_length=200, blank=True, null=True)
    cook_time = models.CharField(max_length=200, blank=True, null=True)
    proof_time = models.CharField(max_length=200, blank=True, null=True)
    serves = models.CharField(max_length=200, blank=True, null=True)

    ingredients = RichTextField(blank=True, null=True)
    method = RichTextField(blank=True, null=True)
    story_time = RichTextField(blank=True, null=True, default="")

    created_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created_on"]

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
