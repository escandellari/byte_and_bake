from datetime import datetime

from django import forms
from django.urls import reverse, reverse_lazy

from .models import Category, Post

cat_choices = list(Category.objects.all().values_list("name", "name"))


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "snippet",
            "author",
            "status",
            "content",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control", "value": "", "id": "author", "type": "hidden"}),
            "category": forms.SelectMultiple(choices=cat_choices, attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "snippet",
            "content",
        )

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }
