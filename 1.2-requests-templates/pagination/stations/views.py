import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as f:
        content = [{k: v for k, v in row.items()} for row in csv.DictReader(f)]
        paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    bus_station = page.object_list
    context = {
         'bus_stations': bus_station,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
