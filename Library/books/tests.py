import pytest
from django.urls import reverse
from authors.models import Author
from django.test import Client
from users.models import CustomUser
from .models import Book


@pytest.fixture
def client():
    CustomUser.objects.create_user(username='testuser', password='testpassword')
    author = Author.objects.create(full_name='Test', date_of_birth='2002-10-12', biography='Test')
    Book.objects.create(title='Test Book', author=author, publication_year=2023, description='This is a test '
                                                                                             'book.')
    return Client()


@pytest.mark.django_db
def test_book_list_view(client):
    url = reverse('books')
    response = client.get(url)
    assert response.status_code == 200
    book_list = response.context['books']
    assert len(book_list) == 1


@pytest.mark.django_db
def test_book_detail_view(client):
    book = Book.objects.get(title='Test Book')
    url = reverse('book', kwargs={'pk': book.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['book'].title == book.title


@pytest.mark.django_db
def test_book_create_view(client):
    client.login(username='testuser', password='testpassword')

    url = reverse('book_create')
    response = client.get(url)
    assert response.status_code == 200

    author = Author.objects.get(full_name='Test')

    data = {
        'title': 'Test Book 2',
        'author': author.pk,
        'publication_year': 2023,
        'description': 'This is a test book.',
    }

    response = client.post(url, data)
    assert response.status_code == 302
