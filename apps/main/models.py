from django.db import models
from apps.utils import custom_upload_path
from django.utils import timezone
# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to=custom_upload_path
    )
    instagram = models.URLField(
        verbose_name='Ссылка на instagram',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Ссылка на facebook',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Ссылка на youtube',
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настроки"
class Artist(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    location = models.TextField(
        verbose_name='адресс'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    photo = models.ImageField(
        upload_to=custom_upload_path,
        verbose_name='Фото'
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"

      
class Event(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Названия события"
    )
    description = models.TextField(
        verbose_name="Описание события"
    )
    image = models.ImageField(
        upload_to=custom_upload_path,
        verbose_name="Фото"
    )
    date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время события"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "Событии"
        
class Blog(models.Model):
    image = models.ImageField(
        upload_to=custom_upload_path,
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )    
    description = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        