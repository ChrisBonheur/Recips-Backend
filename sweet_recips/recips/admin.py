from django.contrib import admin

from .models import Recip, Ingredient

# Register your models here.
admin.site.register(Recip)
admin.site.register(Ingredient)
