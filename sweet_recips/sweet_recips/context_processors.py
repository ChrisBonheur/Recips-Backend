def get_ingredients_from_user(request):
    #get all ingredients from method.POST dict without csrfmiddlewaretoken
    ingredients_from_user = [ingredient for key, ingredient in \
                             request.POST.items() if key != 'csrfmiddlewaretoken']
    return {'ingredients_from_user': ingredients_from_user}
