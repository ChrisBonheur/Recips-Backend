from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="Nom de l'ingredien")
    photo = models.ImageField(null=True)

    class Meta:
        verbose_name = "Ingredient"

    def __str__(self):
        return self.name


class Recip(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la recette", unique=True)
    persons_number = models.IntegerField(null=True)
    preparation = models.TextField(verbose_name="Description de la recette")
    photo = models.ImageField(null=True)
    persons = models.IntegerField(verbose_name="Nombre de personne", null=True)
    date = models.DateField(auto_now=True, verbose_name="Date d'ajout")
    ingredients = models.TextField(null=True)

    class Meta:
        verbose_name = "Recette"

    def __str__(self):
        return self.name

    @property
    def get_ingredients(self):
        ingredients = self.ingredients
        ingredients = ingredients.split(",")
        return ingredients

    # def ingredients_missing(self, *ingredients_from_user):
    #     missing = []
    #     for ingredient in ingredients_from_user:
    #         #regex to verify if ingredient from user is in line of ingredient in sys
    #         regex = '^.+[{}].+'.format(ingredient)
    #         #for each entry in ingredients recip, verify if ingredient from use is in.
    #         if not re.match(regex, [ingredient_system for ingredient_system in self.get_ingredients]):
    #             missing.append(ingredient)
    #
    #     return missing
