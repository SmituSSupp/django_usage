from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=40, blank=False)
    author_id = models.IntegerField(primary_key=True)
    author_description = models.CharField(max_length=200, blank=True, null=True)


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40, blank=False)
    book_description = models.CharField(max_length=200, blank=True, null=True)
    book_authors = models.ManyToManyField(Author, related_name="authors", blank=False)
# Create your models here.
