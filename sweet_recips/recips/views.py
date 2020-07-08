from django.shortcuts import render, redirect
from django.views.generic import ListView
import re
from collections import OrderedDict

from .models import Recip, Ingredient

class Home(ListView):
    model = Recip
    context_object_name = "Recipes"
    template_name = "recips/index.html"
    paginate_by = 5

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

        context = {
            'recipes': recipes,
        }
    else:
        return redirect('recips:home')

    return render(request, 'recips/result.html', context)
