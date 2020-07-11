from django.db import models

import re
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="Nom de l'ingredien")
    photo = models.ImageField(upload_to='icon_ingredients/', null=True)

    class Meta:
        verbose_name = "Ingredient"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.URLField(null=True)

    class Meta:
        verbose_name = "Categorie"


class Recip(models.Model):
    LIST_INGREDIENTS_FROM_USER = []

    name = models.CharField(max_length=100, verbose_name="Nom de la recette", unique=True)
    persons_number = models.IntegerField(null=True)
    preparation = models.TextField(verbose_name="Description de la recette")
    photo = models.URLField(null=True)
    persons = models.IntegerField(verbose_name="Nombre de personne", null=True)
    date = models.DateField(auto_now=True, verbose_name="Date d'ajout")
    ingredients = models.TextField(null=True)
    category = models.ForeignKey(Category, verbose_name="Categorie", on_delete=models.SET_NULL,
                                 null=True)

    class Meta:
        verbose_name = "Recette"

    def __str__(self):
        return self.name

    @property
    def get_ingredients(self):
        ingredients = self.ingredients
        ingredients = ingredients.split(",")
        return ingredients

    @classmethod
    def set_list_ingredients_from_user(cls, list_ingredients):
        """Settings a liste ingredients from user"""
        cls.LIST_INGREDIENTS_FROM_USER = list_ingredients

    @property
    def get_missing_ingredient(self):
        """This function return a missing ingredients list to cook this recip
        before to use it, make sure to set a list ingredients with
        set_list_ingredients_from_user"""
        ingredients_system = self.get_ingredients
        for ingredient in self.LIST_INGREDIENTS_FROM_USER:
            #init ingredient liste from database
            regex = '^.*{}[ a-z]?.*'.format(ingredient)

            for ingredient_system in ingredients_system:
                if re.match(regex, ingredient_system, flags=re.IGNORECASE):
                    ingredients_system.remove(ingredient_system)

        return ingredients_system
