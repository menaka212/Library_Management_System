from django import forms
from .models import Book1

class BookForm(forms.ModelForm):
    class Meta:
        model = Book1
        fields = ['title', 'author', 'published_date', 'isbn']
