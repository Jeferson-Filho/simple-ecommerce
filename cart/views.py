from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from cart.models import Cart, CartProduct, Order, PaymentDetails, ShippingDetails
from user.models import User, Address
import mercadopago

    
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


def payment(request):
    custom_user = User.objects.get(username=request.user.username)
    cart_obj = Cart.objects.filter(user=custom_user, is_active=True).first()
    if not cart_obj:
        return redirect('cart')
    address = Address.objects.filter(email=custom_user).first()
    if not address:
        from django.contrib import messages
        messages.error(request, "Cadastre um endereço antes de finalizar a compra.")
        return redirect('cart')
    cart_products = CartProduct.objects.filter(cart=cart_obj)
    total = 0
    for item in cart_products:
        total += item.product.value * item.quantity
    total += 10  # frete fixo
    if request.method == 'POST' and request.POST.get('confirm_payment') == '1':
        payment = PaymentDetails.objects.create(payment_type='Pix', user=custom_user)
        shipping = ShippingDetails.objects.create(address=address)
        Order.objects.create(cart=cart_obj, payment=payment, shipping=shipping, total=total)
        cart_obj.is_active = False
        cart_obj.save()
        return redirect('orders')
    qr_code, qr_code_base64 = gerar_pix_mp(total, custom_user)
    return render(request, 'payment.html', {
        'qr_code': qr_code,
        'qr_code_base64': qr_code_base64
    })


def checkout(request):
    return redirect('payment')


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

def gerar_pix_mp(valor, custom_user):
    sdk = mercadopago.SDK("TEST-2843815906002759-063001-babb3b54c800ba432a913d48b5444583-239124626")
    nome = custom_user.username
    email = custom_user.email
    cpf = getattr(custom_user, 'document', None) or getattr(custom_user, 'cpf', None)
    payment_data = {
        "transaction_amount": float(valor),
        "description": "Pagamento via Pix",
        "payment_method_id": "pix",
        "payer": {
            "email": email,
            "first_name": nome,
            "identification": {
                "type": "CPF",
                "number": cpf
            },
            "address": {
                "zip_code": "06233-200",
                "street_name": "Av. das Nações Unidas",
                "street_number": "3003",
                "neighborhood": "Bonfim",
                "city": "Osasco",
                "federal_unit": "SP"
            }
        }
    }
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response.get("response", {})
    if "point_of_interaction" in payment and "transaction_data" in payment["point_of_interaction"]:
        qr_code = payment["point_of_interaction"]["transaction_data"]["qr_code"]
        qr_code_base64 = payment["point_of_interaction"]["transaction_data"]["qr_code_base64"]
        return qr_code, qr_code_base64
    else:
        error_message = payment.get("message", "Erro ao gerar pagamento Pix. Verifique os dados e tente novamente.")
        raise Exception(error_message)
