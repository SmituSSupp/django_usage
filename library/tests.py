from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from library.models import Author, Book


class AuthorListTests(APITestCase):
    fixtures = ["test_fixtures/authors.json"]

    def test_create_author(self):
        url = reverse('author-list')
        data = {'author_name': 'Testus Authorus',
                'author_id': 30,
                'author_description': 'testus descriptus'
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.get(author_name__icontains='Testus').author_id, 30)

    def test_create_author_bad_id(self):
        url = reverse('author-list')
        data = {'author_name': 'Testus Authorus',
                'author_id': 1,
                'author_description': 'testus descriptus'
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_author_bad_name(self):
        url = reverse('author-list')
        data = {'author_name': '',
                'author_id': 31,
                'author_description': 'testus descriptus'
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_authors(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.count(), len(response.data))


class AuthorDetailTests(APITestCase):
    fixtures = ["test_fixtures/authors.json"]

    def test_retrieve_author(self):
        url = reverse('author-detail', args=[1])
        response = self.client.get(url, format='json')
        j_steinbeck = {
            "author_name": "John Steinbeck",
            "author_description": "author of mice and men",
            "author_id": 1
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, j_steinbeck)

    def test_update_author(self):
        url = reverse('author-detail', args=[1])
        j_steinbeck = {
            "author_name": "John Steinback",
            "author_description": "author of mice and men",
            "author_id": 1
        }

        response = self.client.put(url, data=j_steinbeck, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(author_id=1).author_name, "John Steinback")

    def test_part_update_author(self):
        url = reverse('author-detail', args=[1])
        j_steinbeck = {
            "author_description": "author of mice and men and more",
            "author_id": 1
        }

        response = self.client.patch(url, data=j_steinbeck, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(author_id=1).author_description, "author of mice and men and more")

    def test_delete_author(self):
        url = reverse('author-detail', args=[1])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Author.objects.filter(author_id=1).exists())

    def test_retrieve_not_found_author(self):
        url = reverse('author-detail', args=[100])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookListTests(APITestCase):
    fixtures = ["test_fixtures/authors.json", "test_fixtures/books.json"]

    def test_create_book(self):
        url = reverse('book-list')
        data = {'book_name': 'Testus Authorus',
                'book_id': 100,
                'book_description': 'testus descriptus',
                'book_authors': [1, 2]
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.get(book_name__icontains='Testus').book_id, 100)

    def test_create_book_bad_id(self):
        url = reverse('book-list')
        data = {'book_name': 'Testus Authorus',
                'book_id': 1,
                'book_description': 'testus descriptus',
                'book_authors': [1, 2]
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_bad_name(self):
        url = reverse('book-list')
        data = {'book_name': '',
                'book_id': 100,
                'book_description': 'testus descriptus',
                'book_authors': [1, 2]
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), len(response.data))


class BookDetailTests(APITestCase):
    fixtures = ["test_fixtures/authors.json", "test_fixtures/books.json"]

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[1])
        response = self.client.get(url, format='json')
        of_m_a_m = {
            "book_name": "Of mice & men",
            "book_description": "book written by John Steinbeck",
            "book_authors": [
                1
            ],
            "book_id": 1
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, of_m_a_m)

    def test_update_book(self):
        url = reverse('book-detail', args=[1])
        of_m_a_m = {
            "book_name": "Of mice & man",
            "book_description": "book written by John Steinbeck",
            "book_authors": [
                1,
                2
            ],
            "book_id": 1
        }

        response = self.client.put(url, data=of_m_a_m, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(book_id=1).book_name, "Of mice & man")
        self.assertEqual(Book.objects.get(book_id=1).book_authors.count(), 2)

    def test_part_update_book(self):
        url = reverse('book-detail', args=[1])
        of_m_a_m = {
            "book_description": "testing stuff",
            "book_id": 1
        }

        response = self.client.patch(url, data=of_m_a_m, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(book_id=1).book_description, "testing stuff")

    def test_delete_book(self):
        url = reverse('book-detail', args=[1])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(book_id=1).exists())

    def test_retrieve_not_found_book(self):
        url = reverse('book-detail', args=[100])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
