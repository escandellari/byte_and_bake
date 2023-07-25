from django import forms

from .models import Category, Recipe

try:
    categories_list = list(Category.objects.all().values_list("name", "name"))
except NameError:
    categories_list = []


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
            "category": forms.Select(choices=categories_list, attrs={"class": "form-control"}),
            "prep_time": forms.TextInput(attrs={"class": "form-control"}),
            "cook_time": forms.TextInput(attrs={"class": "form-control"}),
            "proof_time": forms.TextInput(attrs={"class": "form-control"}),
            "serves": forms.TextInput(attrs={"class": "form-control"}),
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "method": forms.Textarea(attrs={"class": "form-control"}),
            "story_time": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
        }


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
            "category": forms.Select(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
            "prep_time": forms.TextInput(attrs={"class": "form-control"}),
            "cook_time": forms.TextInput(attrs={"class": "form-control"}),
            "proof_time": forms.TextInput(attrs={"class": "form-control"}),
            "serves": forms.TextInput(attrs={"class": "form-control"}),
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "method": forms.Textarea(attrs={"class": "form-control"}),
            "story_time": forms.Textarea(attrs={"class": "form-control"}),
        }
