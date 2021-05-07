import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tattoo.settings')

app = Celery('tattoo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# запуск по времени
app.conf.beat_schedule = {
    'send-spam-every-sunday': {
        'task': 'email_send.tasks.send_beat_email',
        'schedule': crontab()
    }
}
