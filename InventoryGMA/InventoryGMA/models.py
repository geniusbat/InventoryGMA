from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField("Type", max_length=20, primary_key=True)
    description = models.CharField("Description", max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural =("Categories")

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(default="", max_length=100, blank=True)
    category = models.ForeignKey(Category, to_field="name", on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    quantity = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    class Meta:
        verbose_name = ("Thing")
        verbose_name_plural =("Things")

    def __str__(self):
        return self.name + " " + self.description