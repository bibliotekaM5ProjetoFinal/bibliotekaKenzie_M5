from rest_framework import serializers
from .models import Loan
from datetime import datetime, timedelta


class LoanSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    book_title = serializers.SerializerMethodField()

    def get_user_email(self, obj):
        return obj.user.email

    def get_book_title(self, obj):
        return obj.book_copy.book.title

    def update(self, instance: Loan, validated_data: dict) -> Loan:
        instance.devolution_date = datetime.now().date()
        instance.save()
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
