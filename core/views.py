from django.urls import reverse_lazy
from django.views import generic

from core.models import Book


class BooksListView(generic.ListView):
    '''
    class representing a list of all books
    '''
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    '''
    class representing detail info about a book
    '''
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    '''
    class for creating new books
    '''
    model = Book
    template_name = 'book_create.html'
    fields = ('name', 'author', 'price', 'description')


class BookUpdateView(generic.UpdateView):
    '''
    class for updating book info
    '''
    model = Book
    template_name = 'book_edit.html'
    fields = ['name', 'author', 'price', 'description']


class BookDeleteView(generic.DeleteView):
    '''

    '''
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books-list')
