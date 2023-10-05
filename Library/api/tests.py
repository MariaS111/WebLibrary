import pytest
from django.urls import reverse
from rest_framework import status
from .serializers import BookSerializer
from books.models import Book
from authors.models import Author
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_all_books(api_client):
    author1 = Author.objects.create(full_name='Test', date_of_birth='1990-10-09', biography='Test')
    book1 = Book.objects.create(title='Book 1', author=author1, publication_year=1)
    url = reverse('books_api')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_book(api_client):
    author1 = Author.objects.create(full_name='Test Author', date_of_birth='1990-10-09', biography='Test')
    book1 = Book.objects.create(title='Test Book', author=author1, publication_year=1)
    url = reverse('book_api', kwargs={'pk': book1.pk})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Test Book'