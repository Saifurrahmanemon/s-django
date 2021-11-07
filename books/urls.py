from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView, AddReviewView


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("<uuid:pk>/review/", AddReviewView.as_view(), name="create_review"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
