from library.models import Author, Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    book_authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = ['book_name', 'book_description', 'book_authors', 'book_id']


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['author_name', 'author_description', 'book_list', 'author_id']
