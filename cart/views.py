from django.shortcuts import render
from cart.models import Cart, CartProduct
from user.models import User

# Exemplo de view para exibir o carrinho

def cart(request):
    # Busca o usuário customizado pelo username do auth_user
    custom_user = User.objects.get(username=request.user.username)
    # Busca o carrinho ativo do usuário
    cart_obj = Cart.objects.filter(user=custom_user, is_active=True).first()
    cart_items = []
    total = 0
    if cart_obj:
        cart_products = CartProduct.objects.filter(cart=cart_obj)
        for item in cart_products:
            subtotal = item.product.value * item.quantity
            cart_items.append({
                'product': item.product,
                'quantity': item.quantity,
                'subtotal': subtotal
            })
            total += subtotal
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
    })
