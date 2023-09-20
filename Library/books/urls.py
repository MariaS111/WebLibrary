from django.urls import path, include
from .views import BookView, BookDetailView

urlpatterns = [
    path('', BookView.as_view(), name='books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book'),
]