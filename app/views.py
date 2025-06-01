from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/pages/home.html')

def products(request):
    return render(request, 'app/pages/products.html')

def categories(request):
    return render(request, 'app/pages/categories.html')