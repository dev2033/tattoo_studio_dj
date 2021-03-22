from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    name = models.CharField('Имя', max_length=30)
    email = models.EmailField('Email', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
