# Generated by Django 3.1.6 on 2021-05-08 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_send', '0003_auto_20210508_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
    ]
