from crispy_forms.utils import render_crispy_form
from django.shortcuts import redirect, render

from .constants import CUPS_CHOICES, INGREDIENTS_CHOICES
from .forms import ConverterForm, ExampleForm


def example_view(request):
    example_form = ExampleForm()
    if request.method == "POST":
        example_form = ExampleForm(request.POST)
        if example_form.is_valid():
            like_website = request.POST["like_website"]
            favorite_number = request.POST["favorite_number"]
            favorite_color = request.POST["favorite_color"]
            favorite_food = request.POST["favorite_food"]

            submitted = True
            result = like_website + " - " + favorite_number + " - " + favorite_color + " - " + favorite_food

            context = {
                "example_form": example_form,
                "result": result,
                "submitted": submitted,
            }
            return render(request, "converter/index.html", context=context)
    else:
        context = {"example_form": example_form}
        return render(request, "converter/index.html", context)


def converter_view(request):
    converter_form = ConverterForm()
    if request.method == "POST":
        converter_form = ConverterForm(request.POST)

        print(converter_form)
        if converter_form.is_valid():
            uk_ingredient = request.POST["uk_ingredient"]
            cups = request.POST["cups"]

            if uk_ingredient == "oats_uncooked":
                one_cup = 90
            if uk_ingredient in ["desiccated_coconut", "digestive_biscuits"]:
                one_cup = 100
            elif uk_ingredient == "flour_sieved":
                one_cup = 110
            elif uk_ingredient in ["plain_flour", "self_raising_flour", "cornflour", "nuts_ground"]:
                one_cup = 120
            elif uk_ingredient == "icing_sugar":
                one_cup = 125
            elif uk_ingredient in ["nuts_chopped", "breadcrumbs_dry"]:
                one_cup = 150
            elif uk_ingredient in [
                "granulated_sugar",
                "caster_sugar",
                "brown_sugar",
                "coconut_oil",
                "vegetable_oil",
                "sultanas_raisins",
            ]:
                one_cup = 200
            elif uk_ingredient in ["butter", "double_cream"]:
                one_cup = 240
            elif uk_ingredient == "whole_milk":
                one_cup = 245
            elif uk_ingredient == "honey_maple_syrup":
                one_cup = 322
            elif uk_ingredient == "black_treacle":
                one_cup = 340
            elif uk_ingredient == "golden_syrup":
                one_cup = 350

            print(uk_ingredient)
            print(one_cup)
            submitted = True
            result = uk_ingredient + " - " + cups + " - " + str(one_cup)

            context = {
                "converter_form": converter_form,
                "result": result,
                "submitted": submitted,
            }
            return render(request, "converter/index.html", context=context)
    else:
        context = {"converter_form": converter_form}
        return render(request, "converter/index.html", context)
