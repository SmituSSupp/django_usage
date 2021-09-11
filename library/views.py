from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from asgiref.sync import sync_to_async

import asyncio


from django.core.paginator import Paginator


from library.models import Author, Book

from library.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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


async def calculating_imit_books():
    for num in range(0, 4):
        await asyncio.sleep(1)
        print(num)

    return 'smth'


async def calculating_imit_authors():
    for num in range(0, 2):
        await asyncio.sleep(2)
        print(num)

    return 'smth'


async def statistic(request):
    books_num = await sync_to_async(Book.objects.all, thread_sensitive=True)()
    authors_num = await sync_to_async(Author.objects.all, thread_sensitive=True)()
    books_num = await sync_to_async(len)(books_num)
    authors_num = await sync_to_async(len)(authors_num)
    _ = await asyncio.gather(*[calculating_imit_authors(), calculating_imit_books()])

    return JsonResponse({'msg': f"Number of books - {books_num} number of authors - {authors_num}"})
