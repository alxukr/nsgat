from django.db import models
from django.urls import reverse

# Create your models here.


class Links(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    url = models.EmailField(max_length=255, null=False, verbose_name='URL')
    description = models.TextField(null=False, verbose_name='Описание')
    category = models.ForeignKey('LinksCategory', on_delete=models.PROTECT, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['title']


class LinksCategory(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Имя категории')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория ссылок'
        verbose_name_plural = 'Категории ссылок'


class ContactMessage(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Имя')
    title = models.CharField(max_length=255, null=False, verbose_name='Тема')
    email = models.EmailField(max_length=255, null=False, verbose_name='E-mail')
    content = models.TextField(null=False, verbose_name='Текст сообщения')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    user = models.CharField(max_length=255, default='Гость', verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user} : {self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class ScriptCategory(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Имя категории')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scripts', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория скриптов'
        verbose_name_plural = 'Категории скриптов'


class Scripts(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    description = models.TextField(null=False, verbose_name='Описание')
    code = models.TextField(null=False, verbose_name='Код')
    additional = models.TextField(null=True, verbose_name='Дополнительно')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    category = models.ForeignKey('ScriptCategory', on_delete=models.PROTECT, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('script', kwargs={'script_slug': self.slug})

    class Meta:
        verbose_name = 'Скрипт'
        verbose_name_plural = 'Скрипты'
        ordering = ['title']
