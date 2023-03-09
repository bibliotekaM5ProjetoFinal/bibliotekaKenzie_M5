from django.db import models

# Create your models here.


class Loan(models.Model):
    loan_date = models.DateField(auto_now=True)
    devolution_date = models.DateField(null=True)
    book_copy = models.ForeignKey(
        "books.BookCopy", on_delete=models.CASCADE, related_name="loans"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans"
    )
