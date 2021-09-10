from library.models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_name', 'author_id', 'author_description']


class BookSerializer(serializers.ModelSerializer):
    book_authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['book_name', 'book_id', 'book_description', 'book_authors']
