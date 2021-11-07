from django import forms
from django.forms import ModelForm, Textarea, widgets
from .models import Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'review')
        widgets = {'review': Textarea}
