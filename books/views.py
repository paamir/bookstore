from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .froms import CommentForm
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

@login_required()
def book_details_view(request, pk):
    comment_form = CommentForm(request.POST)
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()

    return render(request, 'books/book_details.html',
                  context={
                      'book': book,
                      'book_comments': book_comments,
                      'comment_form': comment_form
                  })


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    context_object_name = 'form'
    fields = ['title', 'author', 'description', 'release_date', 'price', 'cover']


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    context_object_name = 'book'
    fields = ['title', 'author', 'description', 'release_date', 'price']

    def test_func(self):
        book = self.get_object()
        return book.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')

    def test_func(self):
        book = self.get_object()
        return book.user == self.request.user

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.visibility = False
        self.object.save()
        return HttpResponseRedirect(success_url)
