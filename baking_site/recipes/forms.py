from django import forms
from tinymce.widgets import TinyMCE

from .models import Category, Comment, Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "author",
            "category",
            "snippet",
            "image",
            "prep_time",
            "cook_time",
            "proof_time",
            "serves",
            "ingredients",
            "method",
            "story_time",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control", "value": "", "id": "author", "type": "hidden"}),
            "prep_time": forms.TextInput(attrs={"class": "form-control"}),
            "cook_time": forms.TextInput(attrs={"class": "form-control"}),
            "proof_time": forms.TextInput(attrs={"class": "form-control"}),
            "serves": forms.TextInput(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "ingredients": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
            "method": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
            "story_time": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
        }

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "category",
            "snippet",
            "image",
            "story_time",
            "prep_time",
            "cook_time",
            "proof_time",
            "serves",
            "ingredients",
            "method",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "prep_time": forms.TextInput(attrs={"class": "form-control"}),
            "cook_time": forms.TextInput(attrs={"class": "form-control"}),
            "proof_time": forms.TextInput(attrs={"class": "form-control"}),
            "serves": forms.TextInput(attrs={"class": "form-control"}),
            "ingredients": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
            "method": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
            "story_time": TinyMCE(attrs={"class": "form-control", "cols": 80, "rows": 30}),
        }

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
