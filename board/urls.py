"""Маршруты приложения «Доска объявлений»."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ad_list_view, name='ad_list'),
    path('new/', views.ad_create_view, name='ad_create'),
    path('<int:pk>/', views.ad_detail_view, name='ad_detail'),
    path('<int:pk>/edit/', views.ad_edit_view, name='ad_edit'),
    path(
        'comments/<int:pk>/delete/',
        views.comment_delete_view,
        name='comment_delete',
    ),
]
