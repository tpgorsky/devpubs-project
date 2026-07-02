from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Эта строка подключает твой блог:
    path('', include('blog.urls')),
]