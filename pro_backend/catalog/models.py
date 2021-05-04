from django.db import models


class Furniture(models.Model):
    title = models.CharField(max_length=150)
    structure = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Furnitures'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title