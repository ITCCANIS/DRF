from django.urls import path
from django.conf.urls.static import static
from api.views import book_list
from api.views import createBook
from django.conf import settings

urlpatterns = [
    path("getBooks", book_list, name="book-list"),
    path("addBook", createBook, name="createBook"),  # URL for the book list view
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
