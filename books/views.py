from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import Response

from users.permissions import (
    ListingPermissionStaffCreating,
    ListingRetrievingDestroyingPermission,
)
from .models import Book, BookCopy
from .serializers import BookSerializer, BookCopySerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field, extend_schema

# Create your views here.


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ListingPermissionStaffCreating]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(methods=["PUT"], exclude=True)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ListingRetrievingDestroyingPermission]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"


class BookCopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ListingPermissionStaffCreating]

    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    lookup_url_kwarg = "book_pk"

    def list(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_pk"))
        queryset = BookCopy.objects.filter(book=book)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_pk"))
        serializer.save(book=book)


class BookCopyDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ListingRetrievingDestroyingPermission]

    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    lookup_url_kwarg = "book_pk"

    def retrieve(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_pk"))
        copy = get_object_or_404(BookCopy, pk=self.kwargs.get("copy_pk"), book=book)
        serializer = self.get_serializer(copy)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_pk"))
        copy = get_object_or_404(BookCopy, pk=self.kwargs.get("copy_pk"), book=book)
        self.perform_destroy(copy)
        return Response(status=status.HTTP_204_NO_CONTENT)
