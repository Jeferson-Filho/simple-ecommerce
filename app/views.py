from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'app/pages/home.html')

def productDetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/pages/productDetail.html', {
        'product' : product,
    })