from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/templates/home.html')

def products(request):
    return render(request, 'app/templates/products.html')

def categories(request):
    return render(request, 'app/templates/categories.html')