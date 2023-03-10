from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/feeds/", views.FeedBooksView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
    path("books/<int:book_pk>/copies", views.BookCopyView.as_view()),
    path("books/<int:book_pk>/copies/<int:copy_pk>", views.BookCopyDetailView.as_view())
]
