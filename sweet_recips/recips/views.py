from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required

import operator
from functools import reduce
import re
from collections import OrderedDict

from .models import Recip, Ingredient, Quantity

class Home(ListView):
    model = Ingredient
    context_object_name = "ingredients"
    template_name = "recips/index.html"
    # queryset = Ingredient.objects.get(name="Abats")

def result(request, page=1):
    methode = True
    #get all ingredients from method.POST dict without csrfmiddlewaretoken
    ingredients_from_user = [ingredient for key, ingredient in \
                                request.POST.items() if key != 'csrfmiddlewaretoken']
    
    if len(ingredients_from_user) > 0:
        #Object q to place all ingredients from user
        object_q = [Q(ingredient__name=x) for x in ingredients_from_user]
        #This bloc of code clacul and order recipes by missing ingredients number 
        #getting of All recipes with ingredients from user
        q_select = Quantity.objects.filter(reduce(operator.or_, object_q))
        for object_quantity in q_select:
            #we set original ingredient length 
            object_quantity.recipe.ingredients_length = Quantity.objects.filter(\
                recipe=object_quantity.recipe).count()
            length = object_quantity.recipe.ingredients_length
            #here we verify what ingredient recipe is in ingredients_from user to steal length
            #of ingredients origin and to know missing ingredient length 
            for composition in object_quantity.recipe.get_composition:
                if str(composition.ingredient).strip() in ingredients_from_user:
                    length -= 1
            #new length after verification
            object_quantity.recipe.ingredients_length = length
            #new save in database get order by missing number ingredients
            object_quantity.recipe.save()
        
        #New query select after new save for ingredients length and getting by order
        recipes = []
        [recipes.append(obj.recipe) for obj in Quantity.objects.filter(reduce(operator.or_, object_q)).\
            order_by("recipe__ingredients_length") if obj.recipe not in recipes]

        #init method class to set ingredient list from user
        Recip.set_list_ingredients_from_user(ingredients_from_user)

        #Creating for Paginator
        paginator = Paginator(recipes, 8)
        default_page = 1
        try:
            paginator.page(page)
        except PageNotAnInteger as e:
            recipes = paginator.page(default_page)
        except EmptyPage as e:
            recipes = paginator.page(paginator.num_pages)
        else:
            recipes = paginator.page(page)

        context = {
            'recipes': recipes,
            'total_found': paginator.count,
            'test': "salut \n Le monde",
        }
    else:
        return redirect('recips:home')
    
    return render(request, 'recips/result.html', context)

class Detail(DetailView):
    context_object_name = 'recipe'
    model = Recip
    template_name = 'recips/detail.html'

@login_required 
def create(request):
    context = {
        'ingredients': Ingredient.objects.all()
    }
    return render(request, 'recips/create.html', context)
