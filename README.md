# Сайт Тату-студии 'Якорь'

<h3>Запуск проекта:</h3>
1. Скопировать проект, командой:
   
    `git clone https://github.com/dev2033/tattoo_studio_dj.git`
   

2. Установить зависимости:
   
    `pip install -r requirements.txt`
   

3. Перейти в папку с файлом `manage.py` и выполнить миграции, командой:
   
    `python manage.py makemigrations`
   
    `python manage.py migrate`
   

4. Собрать все статические файлы, командой:

    `python manage.py collectstatic`
   

5. Создать суперпользователя, командой:

    `python manage.py createsuperuser`
   

6. Запускаем docker container для redis, командой:
   
    `sudo docker run -d -p 6379:6379 redis`
   
    `sudo docker pull redis`
   

7. Запустить celery worker, командой:
   
    `celery -A tattoo -l info`
   

8. Запустить celery beat, командой:
   
    `celery -A tattoo beat -l info`


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
6. https://redislabs.com/get-started-with-redis/#Option-C