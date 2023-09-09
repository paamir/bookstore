from django.urls import path
from .views import BooksListView, BookDetailsView, BookCreateView

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<int:pk>/', BookDetailsView.as_view(), name='book_details'),
    path('create/', BookCreateView.as_view(), name='book_create'),
]