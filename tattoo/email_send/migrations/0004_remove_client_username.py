# Generated by Django 3.1.6 on 2021-04-04 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_send', '0003_client_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='username',
        ),
    ]