from django.db import models

# Create your models here.

class Post(models.Model):
    post_date = models.DateTimeField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    media = models.ImageField(upload_to='post_media/', null=True, blank=True)
