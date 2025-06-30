from django.urls import path, include
from .views import address

urlpatterns = [
    path('user/', include('user.urls')),
    path('address/', address, name='address'),
]