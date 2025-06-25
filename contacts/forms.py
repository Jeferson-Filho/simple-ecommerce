from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': '*Digite sua mensagem...',
            'rows': 6,
            'style': 'width:100%; border-radius:10px; padding:10px; font-size:16px; resize:none; box-shadow:2px 2px 4px rgba(0,0,0,0.2);'
        })
    )

