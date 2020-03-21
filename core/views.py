from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from hitcount.views import HitCountDetailView

from core.models import Book, Genre, Author


class BooksListView(generic.ListView):
    """
        class representing a list of all books
    """
    model = Book
    template_name = 'core/book_list.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        books = Book.objects.all()
        query = self.request.GET.get("q", "")
        if query:
            books = books.filter(
                Q(name__icontains=query) |
                Q(author__name__icontains=query)
            )
        return books


class BookDetailView(HitCountDetailView):
    """
        class representing detail info about a book
    """
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'
    count_hit = True


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    """
        class for creating new books
    """
    model = Book
    template_name = 'core/book_create.html'
    fields = ('name', 'author', 'price', 'description')


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
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


class AuthorListView(generic.ListView):
    """
        class for representing a list of authors
    """
    model = Author
    template_name = 'core/author_list.html'
    context_object_name = 'authors'
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    """
        class for representing detailed info about the author
    """
    model = Author
    template_name = 'core/author_detail.html'
    context_object_name = 'author'
