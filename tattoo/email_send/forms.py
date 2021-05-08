from django import forms
from django.contrib.auth import get_user_model

from .models import Contact, Client, Record

User = get_user_model()


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваше имя*"
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            "placeholder": "Ваш Email*"
        })
    )

    class Meta:
        model = Contact
        fields = ('name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']

        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Данный почтовый адрес, уже подписан на рассылку!'
            )
        return email


class ClientRecordForm(forms.ModelForm):
    """Форма записи на консультацию пользователя"""
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            "placeholder": "Ваш Email*"
        })
    )
    first_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваше имя*"
        })
    )
    last_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваша фамилия*"
        })
    )
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Ваш номер телефона..."
        })
    )
    message = forms.CharField(
        max_length=1000,
        label='',
        widget=forms.Textarea(attrs={
            "placeholder": "Текст сообщения*"
        })
    )

    class Meta:
        model = Record
        fields = ('email', 'first_name', 'last_name', 'phone', 'message')
