# STREAMING_CHUNK: Setting up URL routing for blog application
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('posts/new/', views.post_create_view, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_edit_view, name='post_edit'),
    # Авторизация (встроенные Django views)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register_view, name='register'),
]