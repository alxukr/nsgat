from django.db import models

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


class LinksCategory(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Имя категории')

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
    user = models.CharField(max_length=255, default='Гость', verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user} : {self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
