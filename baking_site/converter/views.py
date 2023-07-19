from crispy_forms.utils import render_crispy_form
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ConverterForm, TemperatureConversionForm
from .utils import convert_cups_to_grams, convert_temperature


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
    temp_form = TemperatureConversionForm()

    context = {
        "converter_form": converter_form,
        "temp_form": temp_form,
    }

    if request.method == "POST":
        if "ingredient_converter" in request.POST:
            converter_form = ConverterForm(request.POST)
            if converter_form.is_valid():
                uk_ingredient = request.POST["uk_ingredient"]
                cups = request.POST["cups"]
                cups_to_grams = convert_cups_to_grams(uk_ingredient, cups)
                submitted = True
                context["converter_form"] = converter_form
                context["cups_to_grams"] = cups_to_grams
                context["submitted"] = submitted

        if "temperature_converter" in request.POST:
            temp_form = TemperatureConversionForm(request.POST)
            context["temp_form"] = temp_form

            if temp_form.is_valid():
                temperature = request.POST["temperature"]
                conversion = request.POST["conversion"]

                converted_temp = convert_temperature(temperature, conversion)
                submitted_temp = True
                context["converted_temp"] = converted_temp
                context["submitted_temp"] = submitted_temp

        return render(request, "converter/index.html", context=context)

    return render(request, "converter/index.html", context)
