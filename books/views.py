from django.views.generic import ListView, DetailView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'book.special_status'
