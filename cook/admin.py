from django.contrib import admin
from cook.models import Recipe, Ingredient, Tag

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)