from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'app/pages/home.html')
