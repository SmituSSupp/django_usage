from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse


from django.core.paginator import Paginator


from library.models import Author, Book

from library.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def index(request):
    return HttpResponse("welcome to base root of library api")


def library(request):
    books = Book.objects.all()

    page_number = request.GET.get('page')
    author_filter = request.GET.get('author')
    book_name_filter = request.GET.get('title')

    if book_name_filter:
        books = books.filter(book_name__icontains=book_name_filter)

    if author_filter:
        authors = Author.objects.filter(author_name__icontains=author_filter)
        books = books.filter(book_authors__in=authors)

    paginator = Paginator(books, 6)
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})
