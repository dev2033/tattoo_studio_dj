from django.core.mail import send_mail

from tattoo.celery import app
from .service import send
from .models import Contact
from django.conf import settings


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            # Тема письма
            'Вы подписались на рассылку',
            # Контент письма
            'Мы будем присылать вам много СПАМА каждую 1 минуту',
            settings.EMAIL_HOST_USER,
            [contact.email],
            fail_silently=False,
        )
