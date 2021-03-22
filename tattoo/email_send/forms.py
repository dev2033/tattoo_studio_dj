from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваше имя..."
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            "placeholder": "Ваш Email..."
        })
    )

    class Meta:
        model = Contact
        fields = ('name', 'email')
