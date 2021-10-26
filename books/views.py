from django.db import models
from django.db.models import Q
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


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query))
 