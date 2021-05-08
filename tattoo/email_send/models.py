from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Contact(models.Model):
    """Подписка на рассылку по email"""
    name = models.CharField('Имя', max_length=30)
    email = models.EmailField('Email', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Client(models.Model):
    """Клиент студии"""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             null=True, blank=True)
    name = models.CharField('Имя', max_length=100)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона',
                             null=True, blank=True)
    messages = models.TextField('Текст сообщения')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
