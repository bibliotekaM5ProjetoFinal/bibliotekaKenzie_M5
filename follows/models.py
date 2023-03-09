from django.db import models

# Create your models here.


class Follow(models.Model):
    start_following = models.DateField(auto_now=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="following"
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="followed_by"
    )
