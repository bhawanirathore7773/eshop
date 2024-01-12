from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def display_all_catogries():
        return Category.objects.all()

    def __str__(self):
        return self.name
