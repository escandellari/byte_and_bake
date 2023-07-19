from datetime import datetime

from crispy_forms.bootstrap import Div, FormActions, InlineField, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Fieldset, Layout, Row, Submit
from django import forms
from django.urls import reverse_lazy

from .constants import CUPS_CHOICES, INGREDIENTS_WEIGHT_CHOICES


class ConverterForm(forms.Form):
    uk_ingredient = forms.ChoiceField(
        label="UK Ingredient",
        choices=INGREDIENTS_WEIGHT_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    cups = forms.ChoiceField(
        label="Cups",
        choices=CUPS_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )


class TemperatureConversionForm(forms.Form):
    # gas_mark = forms.ChoiceField(
    #     choices=[(x, x) for x in range(1, 10)],
    #     widget=forms.Select(attrs={"class": "form-select"}),
    # )

    temperature = forms.IntegerField(
        label="Temperature",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    conversion = forms.ChoiceField(
        choices=[
            ("gas_mark_f", "Gas Mark -> °Fahrenheit"),
            ("gas_mark_c", "Gas Mark -> °Celsius"),
            ("fahrenheit", "°Fahrenheit -> °Celsius"),
            ("celsius", "°Celsius -> °Fahrenheit"),
        ],
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        temperature = cleaned_data.get("temperature")
        conversion = cleaned_data.get("conversion")

        if conversion in ["gas_mark_f", "gas_mark_c"]:
            if temperature not in range(1, 10):
                # self.add_error("temperature", "Gas Mark chosen, please use 1 to 9")
                raise forms.ValidationError({"temperature": "Gas Mark chosen, please use 1 to 9"})
                # raise forms.ValidationError(
                #     ("Invalid value: %(value)s"),
                #     code="invalid",
                #     params={"value": "42"},
                # )


class StudentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy("converter")
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("submit", "Submit"))

    SUBJECT_CHOICES = (
        (1, "Web Development"),
        (2, "System Programming"),
        (3, "Data Science"),
    )

    # name = forms.CharField(widget=forms.TextInput(attrs={"hx-get": reverse_lazy('converter')}))
    name = forms.CharField()
    age = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "max": datetime.now().date()}),
        required=False,
    )


class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial="1",
        required=True,
    )

    favorite_food = forms.CharField(
        label="What is your favorite food?",
        max_length=80,
        required=True,
    )

    favorite_color = forms.CharField(
        label="What is your favorite color?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Fieldset("Tell us your favorite stuff {{ username }}"),
            Row(
                Column("like_website", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("favorite_number", css_class="form-group col-md-4 mb-0"),
                Column("favorite_color", css_class="form-group col-md-4 mb-0"),
                Column("favorite_food", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            "notes",
            # Fieldset(
            #     "Tell us your favorite stuff {{ username }}",
            #     "like_website",
            #     "favorite_number",
            #     "favorite_color",
            #     "favorite_food",
            #     HTML(
            #         """
            #             <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
            #         """
            #     ),
            #     "notes",
            # ),
            FormActions(
                Submit("save", "Convert"),
            ),
        )
