from django.db import models

# Create your models here.

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Admin', 'Admin'),
    ]
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    user_type = models.CharField(max_length=50, null=False, blank=False)
    document = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    level = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='Cliente', null=True, blank=True)


class Address(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, to_field='email', db_column='email', null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    street = models.CharField(max_length=100, null=False, blank=False)
    number = models.IntegerField(null=True, blank=True)
    complement = models.CharField(max_length=100, null=True, blank=True)
    address_type = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class CreditCard(models.Model):
    card_number = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    validate = models.DateField(null=False, blank=False)
    security_code = models.CharField(max_length=10, null=False, blank=False)
