
from django.test import Client, TestCase
from django.urls import reverse
from .models import Book


class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="good boy",
            author="saifur",
            price='32.323',
        )

    def test_booklisting(self):
        self.assertEqual(f'{self.book.title}', 'good boy')
        self.assertEqual(f'{self.book.author}', 'saifur')
        self.assertEqual(f'{self.book.price}' ,'32.323')

    def test_book_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'good boy')
        self.assertTemplateUsed(response, 'book/book_list.html')

    def test_book_detailview(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/2897')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'good boy')
        self.assertTemplateUsed(response, 'book/book_detail.html')
