from django.db import models
from store.models.customer import Customer
from store.models.product import Product
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=30, default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)



    @staticmethod
    def get_orders_by_customer_id(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')



