from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from cart.models import Cart, CartProduct, Order, PaymentDetails, ShippingDetails
from user.models import User, Address


def cart(request):
    custom_user = User.objects.get(username=request.user.username)
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


def orders(request):
    custom_user = User.objects.get(username=request.user.username)
    user_orders = Order.objects.filter(cart__user=custom_user)
    return render(request, 'orders.html', {
        'orders': user_orders,
    })


def checkout(request):
    custom_user = User.objects.get(username=request.user.username)
    cart_obj = Cart.objects.filter(user=custom_user, is_active=True).first()
    if not cart_obj:
        return redirect('cart')
    address = Address.objects.filter(email=custom_user).first()
    if not address:
        from django.contrib import messages
        messages.error(request, "Cadastre um endereço antes de finalizar a compra.")
        return redirect('cart')
    payment = PaymentDetails.objects.create(payment_type='Cartão', user=custom_user)
    shipping = ShippingDetails.objects.create(address=address)
    # Calcula o total do pedido (produtos + frete)
    cart_products = CartProduct.objects.filter(cart=cart_obj)
    total = 0
    for item in cart_products:
        total += item.product.value * item.quantity
    total += 10  # frete fixo
    Order.objects.create(cart=cart_obj, payment=payment, shipping=shipping, total=total)
    cart_obj.is_active = False
    cart_obj.save()
    return redirect('orders')


def order_details(request, order_id):
    custom_user = User.objects.get(username=request.user.username)
    order = get_object_or_404(Order, id=order_id, cart__user=custom_user)
    cart_products = CartProduct.objects.filter(cart=order.cart)
    product_list = []
    for item in cart_products:
        subtotal = item.product.value * item.quantity
        product_list.append({
            'product': item.product,
            'quantity': item.quantity,
            'subtotal': subtotal
        })
    return render(request, 'orderDetails.html', {'order': order, 'cart_items': product_list})
