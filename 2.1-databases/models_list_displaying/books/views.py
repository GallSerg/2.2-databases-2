from django.shortcuts import render, redirect
from django.db.models import Max, Min
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, template, context)


def pub_date_view(request, p_date):
    template = 'books/book_pagi.html'
    max_pub_date = Book.objects.filter(pub_date__lt=p_date).aggregate(max_pub_date=Max('pub_date'))['max_pub_date']
    min_pub_date = Book.objects.filter(pub_date__gt=p_date).aggregate(min_pub_date=Min('pub_date'))['min_pub_date']
    context = {
        'book_list': Book.objects.filter(pub_date=p_date),
        'pub_date_prev': Book.objects.filter(pub_date=max_pub_date).first(),
        'pub_date_next': Book.objects.filter(pub_date=min_pub_date).first()
    }
    return render(request, template, context)
