from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    phone = models.CharField(max_length=20)
    can_loan = models.BooleanField(default=True, null=False)
    is_superuser = models.BooleanField(default=False)
