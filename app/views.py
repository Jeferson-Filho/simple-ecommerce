from django.shortcuts import render, redirect
from user.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from products.models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == "POST" and "username" in request.POST and "password" in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get("next") or "/"
            return redirect(next_url)
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    images = [
        '/static/img/slide1.jpg',
        '/static/img/slide2.jpg',
        '/static/img/slide3.jpg',
    ]
    products = Product.objects.all()
    return render(request, 'app/pages/home.html', {'images': images, 'products': products})

# View de perfil protegida
def profile(request):
    return render(request, 'app/pages/profile.html')
