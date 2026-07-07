"""Модели приложения «Доска объявлений»: объявления и комментарии."""
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Advertisement(models.Model):
    """Объявление, размещённое пользователем на доске."""

    CATEGORY_CHOICES = [
        ('sale', 'Продажа'),
        ('buy', 'Покупка'),
        ('service', 'Услуги'),
        ('other', 'Разное'),
    ]

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='Цена',
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name='Категория',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='advertisements',
        verbose_name='Автор',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        """Вернуть строковое представление объявления."""
        return self.title

    def get_absolute_url(self):
        """Вернуть URL детальной страницы объявления."""
        return reverse('ad_detail', kwargs={'pk': self.pk})


class AdComment(models.Model):
    """Комментарий пользователя к объявлению."""

    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Объявление',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """Вернуть строковое представление комментария."""
        return f'Комментарий {self.author} к «{self.advertisement}»'
