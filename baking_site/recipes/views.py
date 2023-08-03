from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AddRecipeForm, EditRecipeForm
from .models import Category, Recipe


def recipes_view(request):
    recipe_list = Recipe.objects.all()
    banner = static("img/all_recipes_banner.png")

    return render(
        request,
        "recipes/recipe_index.html",
        {
            "recipe_list": recipe_list,
            "category_name": "All the Recipes",
            "banner": banner,
        },
    )


def category_view(request, name):
    category = Category.objects.get(name=name)
    recipe_list = Recipe.objects.filter(category=category.id)
    banner = static("img/" + category.name + "_banner.png")

    return render(
        request,
        "recipes/recipe_index.html",
        {
            "recipe_list": recipe_list,
            "category_name": name,
            "banner": banner,
        },
    )


def recipe_add_view(request):
    recipe_form = AddRecipeForm()
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.ingredients = request.POST.get("ingredients")
            recipe.method = request.POST.get("steps")
            recipe.save()
            recipe_form.save_m2m()
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


class AddCategoryView(CreateView):
    model = Category
    template_name = "recipes/category_add.html"
    fields = "__all__"
    success_url = reverse_lazy("category_add")
