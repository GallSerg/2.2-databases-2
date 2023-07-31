import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    template_name = 'app/current_time.html'
    msg = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return render(request, template_name, {'msg': msg})


def workdir_view(request):
    lst = os.listdir()
    template_name = 'app/workdir.html'
    return render(request, template_name, {'lst': lst})
