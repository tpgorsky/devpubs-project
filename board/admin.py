"""Регистрация моделей доски объявлений в админ-панели."""
from django.contrib import admin

from .models import AdComment, Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Настройки отображения объявлений в админке."""

    list_display = ('title', 'category', 'price', 'author', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')


@admin.register(AdComment)
class AdCommentAdmin(admin.ModelAdmin):
    """Настройки отображения комментариев в админке."""

    list_display = ('advertisement', 'author', 'created_at')
    list_filter = ('created_at',)
