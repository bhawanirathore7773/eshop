from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Order



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order ,OrderAdmin)