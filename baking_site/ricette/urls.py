from django.urls import path
from django.views.generic import DetailView

from .models import Recipe
from .views import aggiungi_ricetta_view, lista_ricette_view

urlpatterns = [
    path("", lista_ricette_view, name="lista"),
    path("aggiungi/", aggiungi_ricetta_view, name="aggiungi"),
    path("<slug:slug>/", DetailView.as_view(model=Recipe), name="ricetta_dettaglio"),
]
