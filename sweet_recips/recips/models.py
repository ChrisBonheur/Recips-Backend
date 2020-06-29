from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="Nom de l'ingredien")
    photo = models.ImageField(null=True)

    class Meta:
        verbose_name = "Ingredien"

    def __str__(self):
        return self.name


class Recip(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la recette")
    indication = models.TextField(verbose_name="Description de la recette")
    photo = models.ImageField(null=True)
    persons = models.IntegerField(verbose_name="Nombre de personne", null=True)
    date = models.DateField(auto_now=True, verbose_name="Date d'ajout")
    ingredients = models.ManyToManyField(Ingredient, related_name="recettes")
    ingredient_quantity = models.ManyToManyField(Ingredient,through='Quantity',
                                    related_name="+",
                                    verbose_name="Ingredient avc quantité")
    class Meta:
        verbose_name = "Recette"

    def __str__(self):
        return self.name

    @property
    def get_ingredients(self):
        ingredients = Ingredient.objects.filter(recettes__id=self.id)
        return ingredients


class Quantity(models.Model):
    quantity = models.FloatField(verbose_name="Quantité")
    designation = models.CharField(max_length=10, null=True)#after, remove the nullable
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recip = models.ForeignKey(Recip, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "Quantité"
