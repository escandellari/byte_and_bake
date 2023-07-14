from django import forms

from .models import Category, Recipe

# try:
#     categories_list = list(Category.objects.all().values_list("name", "name"))
# except NameError:
#     categories_list = []

categories_list = [
    ("bread", "bread"),
    ("biscuits", "biscuits"),
    ("cakes", "cakes"),
    ("worldwide", "worldwide"),
]


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
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(AddRecipeForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = reverse_lazy("lista")
    #     self.helper.form_method = "POST"
    #     self.helper.layout = Layout(
    #         Div(
    #             Div("title", css_class="form-group col-3"),  # css_class="form-group g-col-6 g-col-md-4"),
    #             Div("snippet", css_class="form-group col-3"),  # css_class="form-group g-col-6 g-col-md-4"),
    #             Div("author", css_class="form-group col-3"),  # css_class="form-group g-col-6 g-col-md-4"),
    #             css_class="row",
    #         ),
    #         Div(
    #             Div("prep_time", css_class="form-group col-3"),
    #             Div("cook_time", css_class="form-group col-3"),
    #             Div("proof_time", css_class="form-group col-3"),
    #             css_class="row",
    #         ),
    #         Div(
    #             Div("serves", css_class="form-group col-3"),
    #             Div("category", css_class="form-group col-3"),
    #             Div("image", css_class="form-group col-3"),
    #             css_class="row",
    #         ),
    #         Div(
    #             Div("ingredients", css_class="form-group col-4"),
    #             css_class="row",
    #         ),
    #         Div(
    #             Div("method", css_class="form-group col-4"),
    #             css_class="row",
    #         ),
    #         FormActions(Submit("submit", "Add Recipe")),
    #     )


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "category",
            "snippet",
            "image",
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
        }
