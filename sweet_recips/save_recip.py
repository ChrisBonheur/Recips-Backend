# import json
# import re
# import time

# recips_list = []

# with open() as fp:
#     recips = json.load(fp)
#     for recip in recips:
#         recips_list.append(recip['recip'])
#
# sauvegarde = 0
# for recip in recips_list:
#     if Recip.objects.filter(name=recip['name']).count() == 0:
#         regex = "^.*([1-9]).*$"
#         person_number = 0
#         if re.match(regex, recip['person_number']):
#             find_re = re.search(regex, recip['person_number'])
#             person_number = find_re.group(1)
#         preparation = " ,".join(recip['preparation'])
#         ingredients = " ,".join(recip['ingredients'][0])
#         url_image = recip['url_image']
#         category = recip['category']
#         name = recip['name']
#         Recip.objects.create(name=name, persons_number=person_number, preparation=preparation, photo=url_image, ingredients=ingredients)
#         sauvegarde += 1
#         print("Sauvegarde : {}".format(sauvegarde))
#         time.sleep(1)
#     else:
#         print('LA RECETTE "{}" EXISTE DÉJÀ: NON AJOUTÉ'.format(recip['name'].upper()))
