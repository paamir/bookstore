from django.urls import path
from .views import BooksListView, book_details_view, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<int:pk>/', book_details_view, name='book_details'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
]