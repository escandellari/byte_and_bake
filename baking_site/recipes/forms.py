from django import forms

from .models import Category, Recipe


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
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "method": forms.Textarea(attrs={"class": "form-control"}),
            "story_time": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
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
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "method": forms.Textarea(attrs={"class": "form-control"}),
            "story_time": forms.Textarea(attrs={"class": "form-control"}),
        }

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
