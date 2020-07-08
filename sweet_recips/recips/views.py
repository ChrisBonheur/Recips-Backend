from django.shortcuts import render, redirect
from django.views.generic import ListView
import re
from collections import OrderedDict

from .models import Recip, Ingredient

class Home(ListView):
    model = Ingredient
    context_object_name = "ingredients"
    template_name = "recips/index.html"

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

        for ingredient in ingredients_from_user:
            #found recips with ingredients from user
            recips_found = Recip.objects.filter(ingredients__icontains=ingredient)
            for recip in recips_found:
                if recip not in recipes:
                    recipes.append(recip)

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
