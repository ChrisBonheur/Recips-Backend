#coding: utf-8
from recips.models import Recip
from django.core.files import File
import json
import re
import time
def echap_french_caracters(sentence, space_caracter="-"):
    """This function transform sentence with some french caracters
    by english term acceptable for variable or fileNames"""
    CARACTERS = ["à", "â", "ä", "é", "è", "ê", "ë", "ï", "î", "ô", "ö", "ù", "û", "ü", "ÿ" ,"ç"]
    u_list = ["ù", "û", "ü"]
    a_list = ["à", "â", "ä"]
    e_list = ["é", "è", "ê", "ë"]
    o_list = ["ô", "ö"]
    i_list = ["ï", "î"]
    name_normal = sentence.strip()
    name_list = list(name_normal)
    name_found = []
    for item in name_list:
        letter = item
        if item in CARACTERS:
            if item in u_list:
                letter = "u"
            elif item in a_list:
                letter = "a"
            elif item in e_list:
                letter = "e"
            elif item in o_list:
                letter = "o"
            elif item in i_list:
                letter = "i"
            elif item == "ÿ":
                letter = "y"
            elif item == "ç":
                letter = "c"
        elif re.match('[^a-zA-Z1-9\.]', item):
            letter = space_caracter
        name_found.append(letter)
    final_name = "".join(name_found)
    final_name = final_name.lower()
    return final_name
# with open('recips/saved_recipes.json') as fp:
#     recips_list = json.load(fp)
# sauvegarde = 0
# for recip in recips_list:
#     if Recip.objects.filter(name=recip['name']).count() == 0:
#         regex = "^.*([1-9]).*$"
#         person_number = recip['person_number']
#         preparation = " ,".join(recip['preparation']).strip()
#         ingredients = " ,".join(recip['ingredients'][0]).strip()
#         url_image = recip['url_image']
#         category = plat
#         name = recip['name']
#         recipe = Recip(name=name, persons=person_number, \
#                              preparation=preparation, photo=url_image, ingredients=ingredients,\
#                              category=category)
#         name_img = echap_french_caracters(name)
#         try:
#             image = File(open('recips/images_recipes/{}.jpg'.format(name_img), 'rb'))
#         except Exception as e:
#             print('No image found')
#         else:
#             recipe.photo = File(open('recips/images_recipes/{}.jpg'.format(name_img), 'rb'))
#             recipe.save()
#             sauvegarde += 1
#             print("Sauvegarde : {}".format(sauvegarde))
#             time.sleep(1)
#     else:
#         print('LA RECETTE "{}" EXISTE DÉJÀ: NON AJOUTÉ'.format(recip['name'].upper()))

# ingredients_list = []

# ingredient = Ingredient(name="Ail")
# ingredient.photo = File.open('https://suisse-nutritionniste.ch/fr/wp-content/uploads/sites/3/2019/10/xail-liste-de-legumes-de-saison.jpg.pagespeed.ic.nKmjX_3KDR.jpg', 'rb')
# ingredient.save()
# with open('ingredients.json') as fp:
#     ingredients = json.load(fp)
#     for ingredient_elt in ingredients:
#         ingredients_list.append(ingredient_elt['ingredient'])
#
# for ingredient in ingredients_list:
#     name = ingredient['name'].strip()
#     url_img = ingredient['img_link']
#     print(url_img)
