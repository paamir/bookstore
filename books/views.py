from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Book


class BooksListView(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(visibility=True).order_by('-creation_date')


# class BookDetailsView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_details.html'
#     context_object_name = 'book'
#
#     def get_context_data(self, **kwargs):
#
#         context = super().get_context_data()
#         context['comments'] = context['book'].comments.all()
#         return context
def book_details_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()

    return render(request, 'books/book_details.html', context={'book': book, 'book_comments': book_comments})

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    context_object_name = 'form'
    fields = ['title', 'author', 'description', 'release_date', 'price', 'cover']


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    context_object_name = 'book'
    fields = ['title', 'author', 'description', 'release_date', 'price']


class BookDeleteView(generic.DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.visibility = False
        self.object.save()
        return HttpResponseRedirect(success_url)
