from django.db import models

# Create your models here.

class Post(models.Model):
    post_date = models.DateField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    media = models.TextField(null=True, blank=True)
