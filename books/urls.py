from django.urls import path
from .views import BooksListView, BookDetailsView

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<int:pk>/', BookDetailsView.as_view(), name='book_details'),
]