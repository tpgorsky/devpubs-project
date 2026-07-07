"""Формы приложения «Доска объявлений»."""
from django import forms

from .models import AdComment, Advertisement


class AdvertisementForm(forms.ModelForm):
    """Форма создания и редактирования объявления."""

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок объявления...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Подробное описание...',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class AdCommentForm(forms.ModelForm):
    """Форма отправки комментария к объявлению."""

    class Meta:
        model = AdComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Оставьте свой комментарий...',
            }),
        }
