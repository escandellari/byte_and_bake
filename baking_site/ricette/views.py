from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from .forms import AddRecipeForm, EditRecipeForm
from .models import Recipe


def recipes_view(request):
    return render(request, "ricette/index.html")


def category_view(request, name):
    recipe_list = Recipe.objects.filter(category=name)
    return render(request, "ricette/category.html", {"recipe_list": recipe_list, "category_name": name})


def recipe_add_view(request):
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
        return render(request, "ricette/recipe_add.html", context=context)


class EditRecipeView(UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    template_name = "ricette/recipe_edit.html"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse_lazy("ricette")
            return HttpResponseRedirect(url)
        else:
            return super(EditRecipeView, self).post(request, *args, **kwargs)


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = "ricette/recipe_delete.html"
    success_url = reverse_lazy("ricette")

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse_lazy("ricette")
            return HttpResponseRedirect(url)
        else:
            return super(DeleteRecipeView, self).post(request, *args, **kwargs)
