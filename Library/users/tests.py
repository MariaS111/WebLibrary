import pytest
from django.urls import reverse
from .models import CustomUser
from django.test import Client


@pytest.fixture
def client():
    user = CustomUser.objects.create(username='testuser')
    user.set_password('testpassword')
    user.save()
    return Client()


@pytest.fixture
def user():
    user = CustomUser.objects.get(username='testuser')
    return user


@pytest.mark.django_db
def test_login_view(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_register_view(client):
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {'username': 'testuser1', 'first_name': 'test', 'last_name': 'user', 'email': 'test@gmail.com','password1': 'testpassword1', 'password2': 'testpassword1'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_view(client, user):
    url = reverse('login')
    client.post(url, {'username': 'testuser', 'password': 'testpassword'})

    url = reverse('logout')
    response = client.post(url)

    assert response.status_code == 200
    assert not response.wsgi_request.user.is_authenticated


