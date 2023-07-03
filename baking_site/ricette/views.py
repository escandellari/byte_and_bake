from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import AddRecipeForm
from .models import Recipe


def lista_ricette_view(request):
    post_list = Recipe.objects.all()
    return render(request, "ricette/lista_ricette.html", {"post_list": post_list})


def aggiungi_ricetta_view(request):
    recipe_form = AddRecipeForm()
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect("lista")
            # Do things
            # Save
            # return render(request, "ricette/aggiungi_ricetta.html", context=context)
    else:
        context = {"recipe_form": recipe_form}
        return render(request, "ricette/aggiungi_ricetta.html", context=context)
