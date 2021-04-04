from django.core.mail import send_mail

from django.conf import settings


def send_appointment(user_email):
    send_mail(
        'Спасибо за обращение!',
        'В ближайшее время мастер с вами свяжется',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )


def send_email(user_email):
    send_mail(
        'Спасибо за подписку',
        'Подписка контент',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
