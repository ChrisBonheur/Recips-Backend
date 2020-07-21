from django.contrib import admin

from .models import Recip, Ingredient, Quantity, Category

# Register your models here.
admin.site.register(Recip)
admin.site.register(Ingredient)
admin.site.register(Quantity)
admin.site.register(Category)
