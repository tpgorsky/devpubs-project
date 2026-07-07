"""Тесты приложения «Доска объявлений»."""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Advertisement


class AdvertisementViewsTest(TestCase):
    """Проверка доступа и основных маршрутов доски объявлений."""

    def setUp(self):
        """Создать тестового пользователя и объявление."""
        self.user = User.objects.create_user('tester', password='pass12345')
        self.ad = Advertisement.objects.create(
            title='Тестовое объявление',
            description='Описание',
            author=self.user,
        )

    def test_list_requires_login(self):
        """Список объявлений недоступен без входа."""
        response = self.client.get(reverse('ad_list'))
        self.assertEqual(response.status_code, 302)

    def test_list_available_after_login(self):
        """Список объявлений открывается после входа."""
        self.client.login(username='tester', password='pass12345')
        response = self.client.get(reverse('ad_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовое объявление')

    def test_detail_available_after_login(self):
        """Детальная страница объявления открывается после входа."""
        self.client.login(username='tester', password='pass12345')
        response = self.client.get(reverse('ad_detail', args=[self.ad.pk]))
        self.assertEqual(response.status_code, 200)
