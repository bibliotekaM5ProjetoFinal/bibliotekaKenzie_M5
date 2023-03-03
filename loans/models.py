from django.db import models

# Create your models here.


class loans(models.Model):
    loan_date = models.DateField(auto_now=True)
    devolution_date = models.DateField()
    book = models.ForeignKey(
        "books.BookCopy", on_delete=models.CASCADE, related_name="users"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans"
    )
