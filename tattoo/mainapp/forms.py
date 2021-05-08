from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm

from email_send.models import Client

User = get_user_model()


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email',
                                       'placeholder': 'Email'})
    )


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "usernameInput",
                   "placeholder": "Логин"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "passInput",
                   "placeholder": "Пароль"}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Пользователь с логином "{username} не найден в системе'
            )
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "usernameInput",
                   "placeholder": "Логин*"}
        )
    )
    username.help_text = "Обязательное поле. Не более 150 символов. " \
                         "Только буквы, цифры и символы @/./+/-/_."
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "passInput",
                   "placeholder": "Пароль*"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "confirm_passInput",
                   "placeholder": "Подтвердите пароль"}
        )
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "phoneInput",
                   "placeholder": "Номер телефона"}
        )
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "addressInput",
                   "placeholder": "Адрес"}
        )
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "first_nameInput",
                   "placeholder": "Имя*"}
        )
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "last_nameInput",
                   "placeholder": "Фамилия*"}
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "emailInput",
                   "placeholder": "Email*"}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['confirm_password'].label = ''
        self.fields['phone'].label = ''
        self.fields['address'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''

    def clean_email(self):
        email = self.cleaned_data['email']
        # domain = email.split('.')[-1]
        # if domain in ['com', 'net']:
        #     raise forms.ValidationError(
        #         f'Регистрация для домена {domain} невозможна'
        #     )
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Данный почтовый адрес уже зарегистрирован в системе'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Имя {username} занято'
            )
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name',
                  'last_name', 'phone', 'address', 'email']
