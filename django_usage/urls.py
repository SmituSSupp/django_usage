"""django_usage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library.views import AuthorViewSet, BookViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns


author_list = AuthorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
author_detail = AuthorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('authors/', author_list, name='author-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
    path('book/', book_list, name='book-list'),
    path('book/<int:pk>/', book_detail, name='book-detail'),
    path('admin/', admin.site.urls),
])
