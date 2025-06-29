from django.db import models
from products.models import Product
from user.models import User, Address, CreditCard

# Create your models here.

class ShippingDetails(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)
    shipping_freight = models.FloatField(null=True, blank=True)


class PaymentDetails(models.Model):
    payment_type = models.CharField(max_length=50, null=False, blank=False)
    card = models.ForeignKey(CreditCard, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    total = models.FloatField(null=False, blank=False)
    is_active = models.BooleanField(default=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False, blank=False)
    payment = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE, null=False, blank=False)
    shipping = models.ForeignKey(ShippingDetails, on_delete=models.CASCADE, null=False, blank=False)