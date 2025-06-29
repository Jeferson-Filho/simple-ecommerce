from django.shortcuts import render

# Exemplo de view para exibir o carrinho

def cart(request):
    # Exemplo: recupere os itens do carrinho da sessão ou do banco
    cart_items = request.session.get('cart_items', [])
    total = sum(item['subtotal'] for item in cart_items) if cart_items else 0
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
    })
