from rest_framework import serializers
from books.models import Book
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'publication_year', 'description', 'cover']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name']