# Сайт Тату-студии 'Якорь'

<h3>Запуск проекта:</h3>
1. Скопировать проект, командой:
```comandline
git clone https://github.com/dev2033/tattoo_studio_dj.git
```
2. Перейти в папку с файлом `manage.py` и выполнить миграции, командой:
```commandline
python manage.py makemigrations
python manage.py migrate
```
3. Собрать все статические файлы, командой:
```commandline
python manage.py collectstatic
```
4. Создать суперпользователя, командой:
```commandline
python manage.py createsuperuser
```

Стек:
- Python
- HTML/CSS/JS 
- Django
- Celery

Полезные ссылки:
1. https://khashtamov.com/ru/celery-best-practices/
2. https://www.hostinger.com.ua/rukovodstva/kak-ispolzovat-smtp-server
3. https://docs.celeryproject.org/en/latest/reference/celery.beat.html
4. https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
5. https://www.youtube.com/watch?v=9RTZP16rvkQ