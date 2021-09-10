from django.contrib import admin
from django.urls import path
from library.views import AuthorViewSet, BookViewSet, index
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
    #path('', index, name='index'),
])
