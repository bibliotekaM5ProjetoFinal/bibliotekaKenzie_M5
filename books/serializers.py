from rest_framework import serializers
from .models import Book, BookCopy
from rest_framework.response import Response


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "synopsis", "copies"]
        depth = 1
        extra_kwargs = {"id": {"read_only": True}}


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ["id", "book", "added_on"]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "book": {"read_only": True},
            "added_on": {"read_only": True},
        }
