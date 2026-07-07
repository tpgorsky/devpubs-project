"""Представления приложения «Доска объявлений» (паттерн MVT)."""
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdCommentForm, AdvertisementForm
from .models import AdComment, Advertisement


@login_required
def ad_list_view(request):
    """Показать список объявлений с пагинацией (5 на страницу)."""
    ads = Advertisement.objects.all()
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'board/ad_list.html', {'page_obj': page_obj})


@login_required
def ad_detail_view(request, pk):
    """Показать объявление, его комментарии и форму отправки комментария."""
    ad = get_object_or_404(Advertisement, pk=pk)
    comments = ad.comments.all()
    paginator = Paginator(comments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = AdCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.advertisement = ad
            comment.author = request.user
            comment.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdCommentForm()
    context = {'ad': ad, 'page_obj': page_obj, 'form': form}
    return render(request, 'board/ad_detail.html', context)


@login_required
def ad_create_view(request):
    """Создать новое объявление от имени текущего пользователя."""
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdvertisementForm()
    context = {'form': form, 'title': 'Подать объявление'}
    return render(request, 'board/ad_form.html', context)


@login_required
def ad_edit_view(request, pk):
    """Отредактировать объявление (доступно только его автору)."""
    ad = get_object_or_404(Advertisement, pk=pk)
    if ad.author != request.user:
        return redirect('ad_list')

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdvertisementForm(instance=ad)
    context = {'form': form, 'title': 'Редактирование объявления'}
    return render(request, 'board/ad_form.html', context)


@login_required
def comment_delete_view(request, pk):
    """Удалить комментарий (доступно его автору или автору объявления)."""
    comment = get_object_or_404(AdComment, pk=pk)
    ad_pk = comment.advertisement.pk
    is_owner = request.user in (comment.author, comment.advertisement.author)
    if request.method == 'POST' and is_owner:
        comment.delete()
    return redirect('ad_detail', pk=ad_pk)
