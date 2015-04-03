# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from cook.models import Recipe, Tag, Ingredient

# Create your views here.
def home(request):
    return render(request, 'home.html', {
            'title': 'Кулинарная книга',
            'recipes': Recipe.objects.all()[:8],
            'tags': Tag.objects.all()[:10]})


def recipes(request, tag_name):
    tag = get_object_or_404(Tag, pk=tag_name)
    recipes = Recipe.objects.filter(tags=tag)

    return render(request, 'recipes.html', {
            'title': '%s' % tag,
            'recipes': recipes,
            'tags': Tag.objects.all()[:10]})

def recipe(request, title):
    recipe = get_object_or_404(Recipe, pk=title)

    return render(request, 'recipe.html', {
            'title': 'Рецепт блюда "%s"' % recipe,
            'recipe': recipe,
            'tags': Tag.objects.all()[:10]})

def ingredients(request, ingredient_name):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_name)
    recipes = Recipe.objects.filter(ingredients=ingredient)

    return render(request, 'recipes.html', {
            'title': 'Рецепты c ингредиентом %s' % ingredient,
            'recipes': recipes,
            'tags': Tag.objects.all()[:10]})