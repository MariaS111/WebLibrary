from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, UpdateView, DeleteView, CreateView
from .models import Book


class BookView(View):
    template_name = 'books/book_list.html'

    def get(self, request):
        query = request.GET.get('query')
        search_parameter = request.GET.get('search_by')
        if query and search_parameter == 'author':
            books = Book.objects.filter(author__full_name__icontains=query)
        elif query and search_parameter == 'title':
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects.select_related()
        return render(request, self.template_name, {'books': books, 'query': query})


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'publication_year', 'description', 'cover']


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'publication_year', 'description', 'cover']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books')
