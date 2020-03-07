from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from core.models import Book, Genre


class BooksListView(generic.ListView):
    """
        class representing a list of all books
    """
    model = Book
    template_name = 'core/book_list.html'
    context_object_name = 'books'
    paginate_by = 4


class BookDetailView(generic.DetailView):
    """
        class representing detail info about a book
    """
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    """
        class for creating new books
    """
    model = Book
    template_name = 'core/book_create.html'
    fields = ('name', 'author', 'price', 'description')


class BookUpdateView(generic.UpdateView):
    """
        class for updating book info
    """
    model = Book
    template_name = 'core/book_edit.html'
    fields = ['name', 'author', 'price', 'description']


class BookDeleteView(generic.DeleteView):
    """
        class for deleting books
    """
    model = Book
    template_name = 'core/book_delete.html'
    success_url = reverse_lazy('books-list')


class GenreListView(generic.ListView):
    """
        class representing a list of all books
    """
    model = Genre
    template_name = 'core/genre_list.html'
    context_object_name = 'genres'
    paginate_by = 4


class GenreDetailView(generic.DetailView):
    """
        class representing detail info about a genre: shows a list of books of this genre
    """
    model = Genre
    template_name = 'core/genre_detail.html'
    context_object_name = 'genre'


class SignUpView(generic.CreateView):
    """
        class for signing up new users
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'core/signup.html'
