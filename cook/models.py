from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    difficulty = models.PositiveSmallIntegerField(default=1)
    instructions = models.TextField(max_length=1000)
    picture = models.URLField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title