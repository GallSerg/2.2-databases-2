from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort != 'name':
        if sort.startswith('min'):
            sort = 'price'
        else:
            sort = '-price'
    context = {
        'phones': Phone.objects.all().order_by(sort)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': i for i in Phone.objects.filter(slug=slug)
    }
    return render(request, template, context)
