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

        #liste of recip object found with liste ingredients missing
        recips = {}

        for ingredient in ingredients_from_user:
            #found recips with ingredients from user
            recips_found = Recip.objects.filter(ingredients__icontains=ingredient)

            for recip in recips_found:
                if recip not in recips.keys():
                    recips[recip] = recip.get_ingredients

                regex = '^.*{}[ a-z]?.*'.format(ingredient)

                for recip_ingredient in recips[recip]:
                    if re.match(regex, recip_ingredient, flags=re.IGNORECASE):
                        recips[recip].remove(recip_ingredient)
                    print(recip_ingredient)

        #dict recip sorted
        recips_sorted = OrderedDict(sorted(recips.items(), key=lambda x: len(x[1]), reverse=False))

        context = {
            'recips': recips_sorted,
        }

    return render(request, 'recips/index.html', context)
