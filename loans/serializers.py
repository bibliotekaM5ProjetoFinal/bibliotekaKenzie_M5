from rest_framework import serializers
from books.models import Book

from follows.models import Follow
from users.models import User
from .models import Loan
from datetime import datetime, timedelta
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class LoanSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    book_title = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.EMAIL)
    def get_user_email(self, obj):
        return obj.user.email

    @extend_schema_field(OpenApiTypes.STR)
    def get_book_title(self, obj):
        return obj.book_copy.book.title

    def update(self, instance: Loan, validated_data: dict) -> Loan:
        instance.devolution_date = datetime.now().date()
        instance.save()

        emails = User.objects.filter(following__book__copies__loans__id=instance.id)

        allEmails = [element.email for element in emails]
        bookName = Book.objects.filter(copies__loans__id=instance.id).first()

        send_mail(
            subject="Book Availiability",
            message=f"The Book,{bookName.title}, has become availiable to Loan.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=allEmails,
            fail_silently=False,
        )
        return instance

    class Meta:
        model = Loan
        fields = [
            "id",
            "loan_date",
            "devolution_date",
            "book_copy",
            "user",
            "user_email",
            "book_title",
        ]
        depths = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "book_copy": {"write_only": True},
            "user": {"write_only": True},
        }
