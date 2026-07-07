"""Корневые маршруты проекта (config.urls)."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Блог (главная, публикации, авторизация)
    path('', include('blog.urls')),
    # Доска объявлений
    path('ads/', include('board.urls')),
]
