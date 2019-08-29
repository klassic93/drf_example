from rest_framework import generics
from books.serializers import BookSerializer
from books.models import Book

from django_filters.rest_framework import DjangoFilterBackend


class BooksListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['popularity', ]


class BookUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BooksFreeListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().filter(user=None)
