from django.contrib import admin
from .models import Recipe, Ingredients


class ingredientInline(admin.TabularInline):
    model = Ingredients

class recipeAdmin(admin.ModelAdmin):
    inlines = [
        ingredientInline,
    ]

admin.site.register(Recipe, recipeAdmin)