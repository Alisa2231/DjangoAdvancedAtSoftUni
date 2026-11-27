from django.urls import path

from books_api.views import ListBooksView, DetailBookView, AuthorsListView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='books'),
    path('book/<int:id>/', DetailBookView.as_view(), name='book-detail'),
    path('authors/', AuthorsListView.as_view(), name='authors'),
]