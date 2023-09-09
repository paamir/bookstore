from django.shortcuts import render
from django.views import generic
from .models import Book


class BooksListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all().order_by('-creation_date')


class BookDetailsView(generic.DetailView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book'


