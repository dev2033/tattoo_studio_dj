from django.core.mail import send_mail

from tattoo.celery import app
from .service import send_appointment, send_email
from .models import Contact
from django.conf import settings


@app.task
def mailing_by_email(user_email):
    """Ответ на запись клинта на консультацию"""
    send_email(user_email)


@app.task
def send_beat_email():
    """Ответ на подписку по email"""
    for contact in Contact.objects.all():
        send_mail(
            # Тема письма
            'Вы подписались на рассылку нашей студии',
            # Контент письма
            'Мы будем присылать вам много СПАМА каждое воскресенье',
            settings.EMAIL_HOST_USER,
            [contact.email],
            fail_silently=False,
        )


@app.task
def appointment_by_email(user_email):
    """Ответ на запись клинта на консультацию"""
    send_appointment(user_email)
