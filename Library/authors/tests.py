import pytest
from django.urls import reverse
from .models import Author
from django.test import Client
from users.models import CustomUser


@pytest.fixture
def client():
    CustomUser.objects.create_user(username='testuser', password='testpassword')
    Author.objects.create(full_name='Test', date_of_birth='2002-10-12', biography='Test')
    return Client()


@pytest.mark.django_db
def test_author_list_view(client):
    url = reverse('authors')
    response = client.get(url)
    assert response.status_code == 200
    authors_list = response.context['authors']
    assert len(authors_list) == 1


@pytest.mark.django_db
def test_author_detail_view(client):
    author = Author.objects.get(full_name='Test')
    url = reverse('author', kwargs={'pk': author.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['author'].full_name == author.full_name


@pytest.mark.django_db
def test_author_create_view(client):
    client.login(username='testuser', password='testpassword')

    url = reverse('author_create')
    response = client.get(url)
    assert response.status_code == 200

    data = {
        'full_name': 'New Author',
        'date_of_birth': '1990-05-15',
        'biography': 'Some bio'
    }
    response = client.post(url, data)
    assert response.status_code == 302

    new_author = Author.objects.get(full_name='New Author')
    assert new_author.full_name == 'New Author'


