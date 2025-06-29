from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
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

# @user_passes_test(lambda u: u.is_staff, login_url='/accounts/login/')
def productCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        value = request.POST.get('value')
        storage = request.POST.get('storage')
        image = request.FILES.get('image')
        if name and description and value and storage is not None:
            product = Product(name=name, description=description, value=value, storage=storage)
            if image:
                product.media = image
            product.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('products')
        else:
            messages.error(request, 'Preencha todos os campos obrigatórios.')
    return render(request, 'products/productCreate.html')