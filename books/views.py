from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
