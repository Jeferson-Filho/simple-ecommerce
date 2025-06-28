from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'document', 'phone', 'user_type']
        labels = {
            'username': 'Nome',
            'email': 'E-mail',
            'document': 'Documento (CPF/CNPJ)',
            'phone': 'Telefone',
            'user_type': 'Tipo de Usuário',
        }
