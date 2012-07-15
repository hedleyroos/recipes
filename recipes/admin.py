from django.contrib import admin

from jmbo.admin import ModelBaseAdmin

from recipes.models import Unit, Ingredient, Recipe, RecipeIngredient


class UnitAdmin(admin.ModelAdmin):
    list_display = ('title',)


class IngredientAdmin(ModelBaseAdmin):
    pass


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient


class RecipeAdmin(ModelBaseAdmin):
    inlines = [RecipeIngredientInline]


admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
