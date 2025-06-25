from django.urls import path
from . import views
from products.views import products

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', products, name='products'),
]
