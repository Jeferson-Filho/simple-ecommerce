from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.conf import settings

# @login_required
def contact(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            user = request.user
            subject = f'Contato via site - {user.username}'
            body = f'Usuário: {user.get_username()} ({user.email})\n\nMensagem:\n{message}'
            destination_email = request.user.email

            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[destination_email],
                fail_silently=False,
            )

            success = True
            form = ContactForm()  # limpa o formulário
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success})
