from datetime import date

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, TextInput, TimeInput

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
