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
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона',
                             null=True, blank=True)
    records = models.ManyToManyField('Record', verbose_name='Записи клиента',
                                     related_name='related_record')

    def __str__(self):
        return "Клиент {} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Record(models.Model):
    """Запись клиента"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               related_name='related_records',
                               verbose_name='Клиент')
    email = models.EmailField('Email', max_length=250)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение',
                               null=True, blank=True)

    def __str__(self):
        return "Клиент {} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
