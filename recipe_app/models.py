from django.db import models
from django.core.urlresolvers import reverse

class Recipe(models.Model):
    def __unicode__(self):
        return self.recipe_name

    recipe_name = models.CharField(max_length=250)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    prep_time = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=50)
    instructions_url = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Ingredients(models.Model):
    def __unicode__(self):
        return self.ingredients

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=1000)