from django import forms
from django.contrib.auth import get_user_model

from .models import Contact, Client


User = get_user_model()


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


class ClientForm(forms.ModelForm):
    """Форма записи на консультацию пользователя"""
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
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваш номер телефона..."
        })
    )
    messages = forms.CharField(
        max_length=1000,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Текст сообщения..."
        })
    )

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'messages')
