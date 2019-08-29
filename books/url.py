from django.urls import path
from books.views import *

urlpatterns = [
    path('books/', BooksListCreateView.as_view()),
    path('books/<int:pk>/', BookUpdateView.as_view()),
    path('books/free/', BooksFreeListView.as_view())
]
