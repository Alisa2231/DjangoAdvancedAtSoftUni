from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books_api.models import Book
from books_api.serializers import BooksSerializer


class ListBooksView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response({'books': serializer.data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailBookView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BooksSerializer(book)
        return Response({'book': serializer.data})

    def put(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BooksSerializer(book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)