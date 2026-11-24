from django.urls import path

from books_api.views import ListBooksView, DetailBookView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='books'),
    path('books/<int:id>/', DetailBookView.as_view(), name='book-detail'),
]