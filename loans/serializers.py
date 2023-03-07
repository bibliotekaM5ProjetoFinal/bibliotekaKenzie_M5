from rest_framework import serializers
from .models import Loan
from datetime import datetime, timedelta

class LoanSerializer(serializers.ModelSerializer):
    
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
            "user"
        ]
        extra_kwargs = {
            "id": {"read_only": True}
        }
