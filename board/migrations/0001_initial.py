"""Начальная миграция: модели Advertisement и AdComment."""
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Создание таблиц объявлений и комментариев."""

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('title', models.CharField(
                    max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(
                    decimal_places=2, default=0, max_digits=12,
                    verbose_name='Цена')),
                ('category', models.CharField(
                    choices=[
                        ('sale', 'Продажа'), ('buy', 'Покупка'),
                        ('service', 'Услуги'), ('other', 'Разное')],
                    default='other', max_length=20,
                    verbose_name='Категория')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='advertisements',
                    to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AdComment',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Дата создания')),
                ('advertisement', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='comments', to='board.advertisement',
                    verbose_name='Объявление')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created_at'],
            },
        ),
    ]
