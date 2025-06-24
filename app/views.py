from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'app/templates/home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'app/templates/products.html', {'products': products})

def produtDetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/templates/productDetail.html', {
        'product' : product,
    })