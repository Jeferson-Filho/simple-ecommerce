from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Address

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.level = 'Cliente'
            user.save()
            from django.contrib.auth.models import User as AuthUser
            if not AuthUser.objects.filter(username=user.username).exists():
                AuthUser.objects.create_user(
                    username=user.username,
                    email=user.email,
                    password=form.cleaned_data['password']
                )
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    if request.method == 'POST':
        user.email = request.POST.get('email', user.email)
        if hasattr(user, 'cpf'):
            user.cpf = request.POST.get('cpf', user.cpf)
        if hasattr(user, 'cnpj'):
            user.cnpj = request.POST.get('cnpj', user.cnpj)
        if hasattr(user, 'phone'):
            user.phone = request.POST.get('phone', user.phone)
        if hasattr(user, 'full_name'):
            user.full_name = request.POST.get('full_name', getattr(user, 'full_name', ''))
        elif hasattr(user, 'first_name') and hasattr(user, 'last_name'):
            full_name = request.POST.get('full_name', '')
            if full_name:
                parts = full_name.split(' ', 1)
                user.first_name = parts[0]
                user.last_name = parts[1] if len(parts) > 1 else ''
        user.save()
        messages.success(request, 'Dados atualizados com sucesso!')
        return redirect('profile')
    return render(request, 'user/profile.html')

@login_required(login_url='/accounts/login/')
def address(request):
    user = request.user
    from .models import User as CustomUser
    custom_user = CustomUser.objects.get(username=user.username)
    address = Address.objects.filter(email=custom_user).first()
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        street = request.POST.get('street', '')
        number = request.POST.get('number', '')
        complement = request.POST.get('complement', '')
        address_type = request.POST.get('address_type', '')
        comment = request.POST.get('comment', '')
        if address:
            address.zip_code = zip_code
            address.country = country
            address.state = state
            address.city = city
            address.street = street
            address.number = number
            address.complement = complement
            address.address_type = address_type
            address.comment = comment
            address.save()
        else:
            address = Address.objects.create(
                email=custom_user,
                zip_code=zip_code,
                country=country,
                state=state,
                city=city,
                street=street,
                number=number,
                complement=complement,
                address_type=address_type,
                comment=comment
            )
        from django.contrib import messages
        messages.success(request, 'Endereço salvo com sucesso!')
        return redirect('address')
    return render(request, 'user/address.html', {'address': address})
