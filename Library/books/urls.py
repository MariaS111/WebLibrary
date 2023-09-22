from django.urls import path, include
from .views import BookView, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BookView.as_view(), name='books'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
