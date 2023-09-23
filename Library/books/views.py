from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, UpdateView, DeleteView, CreateView
from .forms import CommentForm
from .models import Book, Comment


class BookView(View):
    template_name = 'books/book_list.html'
    paginate_by = 5

    def get(self, request):
        query = request.GET.get('query')
        search_parameter = request.GET.get('search_by')
        if query and search_parameter == 'author':
            books = Book.objects.filter(author__full_name__icontains=query)
        elif query and search_parameter == 'title':
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects.select_related()

        paginator = Paginator(books, self.paginate_by)
        page = request.GET.get('page')

        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

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


class CommentCreateView(CreateView):
    def get(self, request, pk):
        form = CommentForm()
        return render(request, 'books/book_add_comment.html', {'form': form, 'pk': pk})

    def post(self, request, pk, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(Book, pk=pk)
            content = form.cleaned_data['content']
            Comment.objects.create(book=book, user=request.user, content=content)
            return HttpResponseRedirect(reverse_lazy('book', kwargs={'pk': pk}))
        else:
            return form
