from django.db import models


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
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона',
                             null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес',
                               null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
