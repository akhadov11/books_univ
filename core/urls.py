from django.urls import path

from core import views


urlpatterns = [
    path('books/', views.BooksListView.as_view(), name="books-list"),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path('book/new/', views.BookCreateView.as_view(), name="book-create"),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name="book-update"),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name="book-delete"),

    path('genres/', views.GenreListView.as_view(), name="genre-list"),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name="genre-detail"),

    path('authors/', views.AuthorListView.as_view(), name="author-list"),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name="author-detail"),

    path('signup/', views.SignUpView.as_view(), name='signup'),
]
