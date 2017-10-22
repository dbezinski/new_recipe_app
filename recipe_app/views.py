from django.views import generic
from django.views.generic.edit import CreateView
from .models import Recipe
from django.http import request
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'recipe_app/index.html'
    context_object_name = "all_recipes"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'all_genres': Recipe.objects.all(),
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(recipe_name__icontains=query)

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe_app/detail.html'

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['recipe_name', 'category', 'image', 'prep_time', 'difficulty', 'instructions_url']


def get_index(request):
    return render(request, 'recipe_app/index.html')

def payment_accepted(request):
    return render(request, 'recipe_app/paymen-accepted.html')


