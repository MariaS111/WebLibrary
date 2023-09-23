from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from books.models import Book


class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book, many=False)
            return Response(serializer.data)
        else:
            books = Book.objects.select_related()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
