from django import forms
from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('review', 'rating', 'book', 'author')
