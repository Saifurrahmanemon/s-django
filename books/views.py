from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.urls import reverse
from django.shortcuts import render, get_list_or_404, redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import FormMixin, CreateView
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Book, Review
from .forms import ReviewForm


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(LoginRequiredMixin,  DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query))


class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'book/create_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.book_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
