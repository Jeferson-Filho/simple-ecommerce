from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    media = models.TextField(null=True, blank=True)
    storage = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
