from django.shortcuts import render
import re
from collections import OrderedDict

from .models import Recip, Ingredient

# Create your views here.
def index(request):
    methode = False
    context = {}

    if request.method == "POST":
        methode = True
        #get all ingredients from method.POST dict without csrfmiddlewaretoken
        ingredients_from_user = [ingredient for key, ingredient in \
                                 request.POST.items() if key != 'csrfmiddlewaretoken']
        #init method class to set ingredient list from user
        Recip.set_list_ingredients_from_user(ingredients_from_user)
        #init list of recip object found by ingredient from user
        recips = []

        for ingredient in ingredients_from_user:
            #found recips with ingredients from user
            recips_found = Recip.objects.filter(ingredients__icontains=ingredient)
            for recip in recips_found:
                if recip not in recips:
                    recips.append(recip)
        context = {
            'recips': recips,
        }

    return render(request, 'recips/index.html', context)
