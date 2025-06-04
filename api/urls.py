from django.urls import path
from api.views import book_list
from api.views import createBook

urlpatterns = [
    path("getBooks", book_list, name="book-list"),
    path("addBook", createBook, name="createBook"),  # URL for the book list view
]
