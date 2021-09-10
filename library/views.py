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


def library(request, author='', name=''):
    books = Book.objects.all()

    paginator = Paginator(books, 4)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})
    #return Response('list.html', {'page_obj': page_obj})
