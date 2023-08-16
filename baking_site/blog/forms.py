from django import forms
from tinymce.widgets import TinyMCE

from .models import Post

categories_list = [
    ("baking", "baking"),
    ("about me", "about me"),
    ("coding", "coding"),
]


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
            "body": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
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
            "body": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
        }
