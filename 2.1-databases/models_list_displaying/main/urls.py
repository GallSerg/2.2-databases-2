from django.contrib import admin
from django.urls import path

from books.converters.date_converter import DateConverter
from django.urls import register_converter
register_converter(DateConverter, 'date')

from books.views import books_view, index, pub_date_view

urlpatterns = [
    path('', index),
    path('books/', books_view, name='books'),
    path('books/<date:p_date>', pub_date_view, name='date'),
    path('admin/', admin.site.urls),
]
