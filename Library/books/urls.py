from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView, CommentCreateView, \
    RateCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/add_comment/', CommentCreateView.as_view(), name='book_add_comment'),
    path('<int:pk>/add_rate/', RateCreateView.as_view(), name='book_add_rate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
