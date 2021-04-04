from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()


class Client(models.Model):
    """Пользователь"""
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона',
                             null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес',
                               null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Master(models.Model):
    """Мастер"""
    name = models.CharField("Имя мастера", max_length=100)
    positions = models.CharField(
        "Должность",
        max_length=70,
        null=True,
        blank=True,
    )
    image = models.ImageField(verbose_name='Изображение')
    about_master = models.TextField(
        "О мастере",
        null=True,
        blank=True,
        help_text='Не обязательно!'
    )
    vk_link = models.CharField(
        'Ссылка на Вконтакте',
        max_length=250,
        blank=True,
        null=True
    )
    inst_link = models.CharField(
        'Ссылка на Инстаграм',
        max_length=250,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_master', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"
        ordering = ["name"]


class Post(models.Model):
    """Блог"""
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name="Имя мастера"
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='posts',
        verbose_name='Теги'
    )
    title = models.CharField("Название поста", max_length=100)
    slug = models.SlugField('Url', max_length=255, unique=True)
    content = models.TextField('Контент', blank=True)
    views = models.IntegerField('Колличество просмотров', default=0)
    image = models.ImageField("Фото", blank=True, null=True,
                              help_text='Не обязательно!')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]


class TattooCategory(models.Model):
    """Виды категорий"""
    name = models.CharField(
        'Название категории тату для главной страницы',
        max_length=100
    )
    content = models.CharField(
        'Контент',
        max_length=250,
        help_text='Краткое описание про вид татуировок'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид татуировки'
        verbose_name_plural = 'Виды татуировок'


class Tag(models.Model):
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('Url', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class WorkMaster(models.Model):
    """Работы мастеров для портфолио"""
    name = models.CharField(
        'Название тату',
        max_length=50,
        blank=True,
        null=True,
        help_text='Не обязательно, не где не задействуется! '
                  'Пример: Имя Фамилия мастера'
    )
    slug = models.SlugField('Url', max_length=50, unique=False)
    master_name = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='work_master',
        verbose_name='Мастер'
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Теги'
    )
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return str(self.pk) + " " + str(self.name)

    # def get_absolute_url(self):
    #     return reverse('works', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Работа мастера'
        verbose_name_plural = 'Работа мастеров'
        ordering = ['master_name']


class AboutStudio(models.Model):
    """О студии"""
    content = models.TextField('Контент')

    def __str__(self):
        return 'О студии'

    class Meta:
        verbose_name = 'О студии'
        verbose_name_plural = 'О студии'
