from django.forms import ModelForm
from equipsmith_dev.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page', )