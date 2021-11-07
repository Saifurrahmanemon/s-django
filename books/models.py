from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls.base import reverse_lazy


# this is our published books model


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField(
        default=datetime.date.today, verbose_name='book published date')
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    review = models.CharField(max_length=500)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        blank=True, null=True, help_text='the ratings from reviewers',
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(null=True)

    def __str__(self):
        return self.review
