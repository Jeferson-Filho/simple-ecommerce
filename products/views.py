from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from cart.models import Cart
from cart.models import CartProduct
from .models import Product
from user.models import User

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
    
def productDetail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total = product.value * quantity + 10.0
        custom_user = User.objects.get(username=request.user.username)
        cart, created = Cart.objects.get_or_create(user=custom_user, is_active=True, defaults={'total': total})
        item, created = CartProduct.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()
        messages.success(request, 'Produto adicionado ao carrinho!')
        return redirect('cart')
    
    return render(request, 'products/productDetail.html', {
        'product': product,
        'range': range(1, product.storage + 1),
        'frete': 10.0,
    })

@user_passes_test(lambda u: u.is_staff, login_url='/accounts/login/')
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