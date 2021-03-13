from django.forms import ModelForm
from books.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'fiction_or_non']