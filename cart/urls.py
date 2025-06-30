from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/<int:order_id>/', views.order_details, name='orderDetails'),
]
