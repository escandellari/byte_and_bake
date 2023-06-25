from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, TextInput, TimeInput

from .constants import CUPS_CHOICES, INGREDIENTS_CHOICES
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    #     widgets = {
    #         "date": DateInput(attrs={"type": "date"}),
    #         "start": TimeInput(attrs={"type": "time"}),
    #         "duration": TextInput(attrs={"type": "number", "min": "1", "max": "4"}),
    #     }

    # def clean_date(self):
    #     input_date = self.cleaned_data.get("date")
    #     if input_date < date.today():
    #         raise ValidationError("Meeting cannot be in the past")
    #     return input_date


class ConverterForm(forms.Form):
    ingredients = forms.CharField(label="Ingredients", max_length=25, widget=forms.Select(choices=INGREDIENTS_CHOICES))
    cups = forms.CharField(label="Cups", max_length=25, widget=forms.Select(choices=CUPS_CHOICES))
    grams = forms.CharField(label="grams", max_length=25)

    # class Meta:
    #     # model = Post
    #     fields = "__all__"

    # def __str__(self):
    #     return self.ingredients
