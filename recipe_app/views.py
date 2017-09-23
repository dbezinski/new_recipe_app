from django.views import generic
from django.views.generic.edit import CreateView
from .models import Recipe

from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'recipe_app/index.html'
    context_object_name = "all_recipes"

    def get_queryset(self):
        return Recipe.objects.all()

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe_app/detail.html'

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_name', 'category', 'image', 'prep_time', 'difficulty', 'instructions_url']

def get_index(request):
    return render(request, 'recipe_app/index.html')