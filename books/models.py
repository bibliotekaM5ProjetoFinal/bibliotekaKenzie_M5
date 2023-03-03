from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    synopsis = models.TextField()


class BookCopy(models.Model):
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="book"
    )
    added_on = models.DateField(auto_now=True)
