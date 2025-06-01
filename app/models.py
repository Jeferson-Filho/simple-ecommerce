from django.db import models

# Create your models here.
# app/models.py

from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    user_type = models.CharField(max_length=50, null=False, blank=False)
    document = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)


class Address(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='email', db_column='email', null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    street = models.CharField(max_length=100, null=False, blank=False)
    number = models.IntegerField(null=True, blank=True)
    complement = models.CharField(max_length=100, null=True, blank=True)
    address_type = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


class Post(models.Model):
    post_date = models.DateField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    media = models.TextField(null=True, blank=True)


class ShippingDetails(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)
    shipping_freight = models.FloatField(null=True, blank=True)


class CreditCard(models.Model):
    card_number = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    validate = models.DateField(null=False, blank=False)
    security_code = models.CharField(max_length=10, null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    media = models.TextField(null=True, blank=True)
    storage = models.IntegerField(null=True, blank=True)


class PaymentDetails(models.Model):
    payment_type = models.CharField(max_length=50, null=False, blank=False)
    card = models.ForeignKey(CreditCard, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, blank=False)


class Carts(models.Model):
    total = models.FloatField(null=False, blank=False)


class Order(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE, null=False, blank=False)
    payment = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE, null=False, blank=False)
    shipping = models.ForeignKey(ShippingDetails, on_delete=models.CASCADE, null=False, blank=False)


class CartProduct(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
