from django.contrib import admin

from books_api.models import Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pages', 'description']