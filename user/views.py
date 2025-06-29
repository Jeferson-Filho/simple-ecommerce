from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            from django.contrib.auth.hashers import make_password
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def profile(request):
    return render(request, 'user/profile.html')
