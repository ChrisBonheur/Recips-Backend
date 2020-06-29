from django.shortcuts import render
import re

from .models import Recip, Ingredient, Quantity

# Create your views here.
def index(request):
    methode = False
    context = {}

    if request.method == "POST":
        methode = True
        #get all ingredients from method.POST dict without csrfmiddlewaretoken
        ingredients_from_user = [ingredient for key, ingredient in \
                                 request.POST.items() if key != 'csrfmiddlewaretoken']

        #liste of recip found with liste ingredients from user
        recips = []
        for ingredient in ingredients_from_user:
            recips_found = Recip.objects.filter(ingredients__name=ingredient)
            recips += recips_found

        #constitute number repition of a ingredients in recips liste
        recips_miss_ingredients = {}
        for recip in recips:
            if recip not in recips_miss_ingredients.keys():
                #Ingredian list missing in recips
                ingredients_miss = [ingredient.name for ingredient in recip.get_ingredients \
                                    if ingredient.name not in ingredients_from_user]
                recips_miss_ingredients[recip] = ingredients_miss

                print(recips_miss_ingredients)

        context = {
            'recips_miss_ingredients': recips_miss_ingredients,
        }

    return render(request, 'recips/index.html', context)
