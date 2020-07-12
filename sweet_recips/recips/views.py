from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
import operator
from functools import reduce
import re
from collections import OrderedDict

from .models import Recip, Ingredient

class Home(ListView):
    model = Ingredient
    context_object_name = "ingredients"
    template_name = "recips/index.html"
    # queryset = Ingredient.objects.get(name="Abats")

def result(request):
    if request.method == "POST":
        methode = True
        #get all ingredients from method.POST dict without csrfmiddlewaretoken
        ingredients_from_user = [ingredient for key, ingredient in \
                                 request.POST.items() if key != 'csrfmiddlewaretoken']
        #init method class to set ingredient list from user
        Recip.set_list_ingredients_from_user(ingredients_from_user)
        #init list of recip object found by ingredient from user
        recipes = []
        recips_found = Recip.objects.filter(reduce(operator.or_, \
            [Q(ingredients__icontains=ingredient) for ingredient in ingredients_from_user]))
        #add recipes_found in recipes list 
        recipes += recips_found

        #Order a list result recips by number of ingredients found in
        recipes_length = len(recipes)
        for i in range(recipes_length):
            for j in range(recipes_length):
                #lenght of a values() in dict
                values_length_i = recipes[i].get_missing_ingredient
                values_length_i = len(values_length_i)
                values_length_j = recipes[j].get_missing_ingredient
                values_length_j = len(values_length_j)

                if values_length_i <= values_length_j and i <= recipes_length:
                    recipes[i], recipes[j] = recipes[j], recipes[i]

        context = {
            'recipes': recipes,
        }
    else:
        return redirect('recips:home')

    return render(request, 'recips/result.html', context)

class Detail(DetailView):
    context_object_name = 'recipe'
    model = Recip
    template_name = 'recips/detail.html'
