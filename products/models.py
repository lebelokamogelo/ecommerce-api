from django.db import models
from accounts.models import User

class Addres(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    street = models.CharField(max_length=255, verbose_name='Street')
    city = models.CharField(max_length=255, verbose_name='City')
    zip_code = models.CharField(max_length=255, verbose_name='Zip Code')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Addres, null=True, on_delete=models.SET_NULL)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Categorie(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
