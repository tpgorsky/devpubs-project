"""Конфигурация приложения «Доска объявлений»."""
from django.apps import AppConfig


class BoardConfig(AppConfig):
    """Класс конфигурации приложения board."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
    verbose_name = 'Доска объявлений'
