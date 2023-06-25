from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import ConverterForm
from .models import Post


def category_view(request, name):
    post_list = Post.objects.filter(category__name=name)
    return render(request, "blog/category.html", {"post_list": post_list, "category_name": name})


def worldwide_view(request):
    return render(request, "blog/worldwide.html")


def recipes_view(request):
    return render(request, "blog/recipes.html")


def cheatsheets_view(request):
    form = ConverterForm()
    if request.method == "POST":
        ingredient = request.POST["ingredients"]
        cups = request.POST["cups"]
        grams = request.POST["grams"]
        print(ingredient, cups, grams)
        #     #     if form.is_valid():
        #     #         # process the data in form.cleaned_data as required
        #     #         # ...
        #     #         # redirect to a new URL:
        #     #         # return HttpResponseRedirect("/thanks/")
        #     #         return render(request, "blog/cheatsheets.html")
        context = {"result": ingredient}
        return render(request, "blog/cheatsheets.html", context=context)
    else:
        return render(request, "blog/cheatsheets.html", {"form": form})


# def calculateConversion(request):
#     # if this is a POST request we need to process the form data
#     # if request.method == "POST":
#     #     # create a form instance and populate it with data from the request:
#     #     form = ConverterForm(request.POST)
#     #     # check whether it's valid:
#     #     if form.is_valid():
#     #         # process the data in form.cleaned_data as required
#     #         # ...
#     #         # redirect to a new URL:
#     #         # return HttpResponseRedirect("/thanks/")
#     #         return render(request, "blog/cheatsheets.html")

#     # # if a GET (or any other method) we'll create a blank form
#     # else:
#     form = ConverterForm()
#     print(form)
#     print("***************************************")

#     return render(request, "blog/cheatsheets.html", {"form": form})
