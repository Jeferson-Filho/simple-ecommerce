from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'storage', 'created_at']
    search_fields = ['name', 'description']
