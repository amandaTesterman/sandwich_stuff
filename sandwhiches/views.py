from django.shortcuts import render
from django.views import View 
from django.http import Http404
import random
# Create your views here.
ingredients = {
    'meats' : ['turkey', 'steak', 'chicken', 'bacon'],
    'cheeses' : ['provolone', 'munster', 'perpper jack'],
    'toppings' : ['onions', 'tomato', 'lettuce', 'pickles'],
}

class SandwhichesView(View):
    def get(self, request ):
        return render (
            request = request, 
            template_name = "sandwhiches.html",
            context = {'ingredients': ingredients.keys()},

        )
class IngredientsView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')

        return render (
            request = request,
            template_name = 'ingredientsList.html',
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type' : ingredient_type,
            }
        )

class RandomView(View):
    def get(self, request):
        
        meat = random.choice(ingredients['meats'])
        cheese = random.choice(ingredients['cheeses'])
        topping = random.choice(ingredients['toppings'])
        return render (
            request = request,
            template_name = 'random.html',
            context = {
                'sandwhich_meat': meat,
                'cheese' : cheese,
                'topping': topping
            }
        )
