from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe, Ingredient

# Create your views here.
def home(request):
    recipts = Recipe.objects.all()
    ingredients = Ingredient.objects.all()
    context = {
            'recipts': recipts,
            'ingredients': ingredients
            }
    return render(request, 'app/home.html', context)

def recipes_id_filter(request, pk):

    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'app/recipe.html', context)

def ingredients_id_filter(request, pk):

    for el in Recipe.objects.all():
        for ing in el.ingredients.all():
            if ing.id == pk:
                recipe = el
    context = {'recipe': recipe}
    return render(request, 'app/recipe.html', context)
