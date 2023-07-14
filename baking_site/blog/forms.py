from django import forms

from .models import Category, Post

try:
    categories_list = list(Category.objects.all().values_list("category_name", "category_name"))
except NameError:
    categories_list = []


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "category", "snippet", "header_image", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "author": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "author", "type": "hidden"}),
            "category": forms.Select(
                choices=categories_list,
                attrs={
                    "class": "form-control",
                },
            ),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "snippet", "category", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "category": forms.Select(
                choices=categories_list,
                attrs={
                    "class": "form-control",
                },
            ),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }
