from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView

urlpatterns = [
    path('', AuthorListView.as_view(), name='authors'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('create/', AuthorCreateView.as_view(), name='author_create')
]
