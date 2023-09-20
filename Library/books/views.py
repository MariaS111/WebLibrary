from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


class BookView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
