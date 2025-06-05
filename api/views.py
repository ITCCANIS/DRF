from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from api.models import Book
from api.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
@api_view(["GET"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    return Response({"error": "Method not allowed"}, status=405)


@api_view(["POST"])
def createBook(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response(
        {"error": "Method not allowed"}, status=405
    )  # Handle non-POST requests
