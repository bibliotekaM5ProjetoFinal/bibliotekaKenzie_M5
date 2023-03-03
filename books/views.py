from django.shortcuts import render
from rest_framework import generics

# Create your views here.


class BookView(generics.CreateAPIView):
    ...


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...


class BookCopyView(generics.CreateAPIView):
    ...


class BookCopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...
