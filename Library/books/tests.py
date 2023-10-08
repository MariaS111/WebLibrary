import pytest
from django.urls import reverse
from authors.models import Author
from django.test import Client
from users.models import CustomUser
from .models import Book, Comment


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


@pytest.mark.django_db
def test_book_update_view(client):
    client.login(username='testuser', password='testpassword')

    book = Book.objects.get(title='Test Book')
    url = reverse('book_update', kwargs={'pk': book.pk})

    response = client.get(url)
    assert response.status_code == 200

    author = Author.objects.get(full_name='Test')

    data = {
        'title': 'Test Book',
        'author': author.pk,
        'publication_year': 2020,
        'description': 'This is updated test book.',
    }

    response = client.post(url, data)
    assert response.status_code == 302
    assert Book.objects.get(pk=book.pk).description == 'This is updated test book.'
    assert Book.objects.get(pk=book.pk).publication_year == 2020


@pytest.mark.django_db
def test_book_delete_view(client):
    client.login(username='testuser', password='testpassword')

    book = Book.objects.get(title='Test Book')
    url = reverse('book_delete', kwargs={'pk': book.pk})

    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 302
    assert not Book.objects.filter(pk=book.pk).exists()


@pytest.mark.django_db
def test_comment_create_view(client):
    client.login(username='testuser', password='testpassword')
    book = Book.objects.get(title='Test Book')
    url = reverse('book_add_comment', kwargs={'pk': book.pk})

    response = client.get(url)
    assert response.status_code == 200

    user = response.wsgi_request.user
    response = client.post(url, {'user': user.pk, 'book': book.pk, 'content': 'This is a test comment.'})
    assert response.status_code == 302
    assert Comment.objects.filter(content='This is a test comment.').exists()

    comment = Comment.objects.get(content='This is a test comment.')
    assert comment.book == book
    assert comment.user == user
