from django import template
from recips.models import Ingredient
import re

register = template.Library()

@register.filter(name="photo")
def get_image_from_ingredients(ingredient_elt):
    ingredients = Ingredient.objects.all()
    print(ingredient_elt)
    image_url = "replace a default link_image in templatetags"
    for ingredient in ingredients:
        regex = '^.*{}.*'.format(ingredient)
        if re.match(regex, ingredient_elt):
            image_url = ingredient.photo.url

    return image_url
