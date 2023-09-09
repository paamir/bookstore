from django.shortcuts import render
from django.urls import reverse_lazy
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


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    context_object_name = 'form'
    fields = ['title', 'author', 'description', 'release_date', 'price']


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    context_object_name = 'book'
    fields = ['title', 'author', 'description', 'release_date', 'price']


# class BookDeleteView(generic.DeleteView):
#     model = Book
#     template_name = 'books/book_delete.html'
#     success_url = reverse_lazy('books_list')
