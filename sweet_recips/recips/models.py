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
    photo = models.ImageField(upload_to="images_category", null=True)

    class Meta:
        verbose_name = "Categorie"


class Recip(models.Model):
    LIST_INGREDIENTS_FROM_USER = []

    name = models.CharField(max_length=100, verbose_name="Nom de la recette", unique=True)
    preparation = models.TextField(verbose_name="Description de la recette")
    photo = models.ImageField(upload_to="images_recipes",null=True)
    persons = models.IntegerField(verbose_name="Nombre de personne", null=True)
    date = models.DateField(auto_now=True, verbose_name="Date d'ajout")
    category = models.ForeignKey(Category, verbose_name="Categorie", on_delete=models.SET_NULL,
                                 null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='+', through='Quantity')
    ingredients_length = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Recette"
    
    @property
    def get_composition(self):
        composition = Quantity.objects.filter(recipe__id=self.id)
        return Quantity.objects.filter(recipe__id=self.id).order_by("recipe__ingredients_length")

    @classmethod
    def set_list_ingredients_from_user(cls, list_ingredients): 
        """Settings a liste ingredients from user"""
        cls.LIST_INGREDIENTS_FROM_USER = list_ingredients

    @property
    def get_missing_ingredient(self):
        """This function return a missing ingredients list to cook this recip
        before to use it, make sure to set a list ingredients with
        set_list_ingredients_from_user"""
        ingredients_missing = [composition for composition in self.get_composition if \
            str(composition.ingredient).strip() not in self.LIST_INGREDIENTS_FROM_USER]
  
        return ingredients_missing

class Quantity(models.Model):
    indication = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recip, on_delete=models.CASCADE)