from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
    
def productDetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/productDetail.html', {
        'product': product,
        'range': range(1, product.storage + 1),
        'frete': 10.0,
    })