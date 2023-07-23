from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AddRecipeForm, EditRecipeForm
from .models import Recipe


def recipes_view(request):
    return render(request, "recipes/index.html")


def category_view(request, name):
    recipe_list = Recipe.objects.filter(category=name)
    return render(request, "recipes/category.html", {"recipe_list": recipe_list, "category_name": name})


def recipe_add_view(request):
    recipe_form = AddRecipeForm()
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            return redirect(reverse("recipe_detail", kwargs={"slug": recipe.slug}))
        else:
            print(recipe_form.errors.as_data())
            print("***********************")
    else:
        context = {"recipe_form": recipe_form}
        return render(request, "recipes/recipe_add.html", context=context)


class EditRecipeView(UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    template_name = "recipes/recipe_edit.html"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse("recipe_detail", kwargs={"slug": self.kwargs["slug"]})
            return HttpResponseRedirect(url)
        else:
            return super(EditRecipeView, self).post(request, *args, **kwargs)


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_delete.html"
    success_url = reverse_lazy("recipes")

    def post(self, request, *args, **kwargs):
        if not "cancel" in request.POST:
            return super(DeleteRecipeView, self).post(request, *args, **kwargs)
