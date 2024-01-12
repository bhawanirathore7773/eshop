from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey(Category ,on_delete= models.CASCADE, default= 1)
    description = models.CharField(max_length=200, default='description')
    image = models.ImageField(upload_to='uploads/product')

    @staticmethod
    def cart_value_sum(dict):
        sum = 0
        for dic in dict:
            sum += int(dic)

        return sum

    @staticmethod
    def display_all_product():
        return Product.objects.all

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def display_all_product_by_category_id(category_id):
        if category_id :
            return Product.objects.filter(category = category_id)
        else:
            return Product.display_all_product();



