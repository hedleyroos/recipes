from django.db import models

from ckeditor.fields import RichTextField
from jmbo.models import ModelBase


class Unit(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Ingredient(ModelBase):
    pass


class Recipe(ModelBase):
    serves = models.PositiveIntegerField()
    instructions = RichTextField(
        blank=True,
        null=True,
    )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    unit = models.ForeignKey(Unit)
    amount = models.FloatField()

