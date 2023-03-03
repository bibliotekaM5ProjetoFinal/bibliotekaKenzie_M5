from django.shortcuts import render
from rest_framework import generics

# Create your views here.


class LoanView(generics.CreateAPIView):
    ...


class LoanDetailView(generics.RetrieveDestroyAPIView):
    ...
