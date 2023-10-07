from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, ListView
from .models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            authors = paginator.page(page)
        except PageNotAnInteger:
            authors = paginator.page(1)
        except EmptyPage:
            authors = paginator.page(paginator.num_pages)
        context['authors'] = authors
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'


@method_decorator(login_required, name='dispatch')
class AuthorCreateView(CreateView):
    model = Author
    template_name = 'authors/author_create.html'
    fields = ['full_name', 'date_of_birth', 'biography']
