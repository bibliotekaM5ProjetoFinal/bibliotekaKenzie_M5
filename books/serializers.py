from django.shortcuts import get_object_or_404
from rest_framework import serializers

from users.models import User
from .models import Book, BookCopy
from rest_framework.response import Response
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class BookCopyFieldSerializer(serializers.ModelSerializer):
    @extend_schema_field(OpenApiTypes.OBJECT)
    class LoanListingField(serializers.RelatedField):
        def to_representation(self, value):
            loan = {
                "id": value.id,
                "loan_date": value.loan_date,
                "devolution_date": value.devolution_date,
                "user_username": value.user.username,
            }
            return loan

    loans = LoanListingField(many=True, read_only=True)

    class Meta:
        model = BookCopy
        fields = ["id", "added_on", "loans"]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "added_on": {"read_only": True},
        }


@extend_schema_field(OpenApiTypes.OBJECT)
class FollowedListingField(serializers.RelatedField):
    def to_representation(self, value):
        follow = {"username": value.user.username, "since": value.start_following}
        return follow


class BookSerializer(serializers.ModelSerializer):
    followed_by = FollowedListingField(many=True, read_only=True)
    copies = BookCopyFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "synopsis", "copies", "followed_by"]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
        }


class BookCopySerializer(serializers.ModelSerializer):
    @extend_schema_field(OpenApiTypes.OBJECT)
    class LoanListingField(serializers.RelatedField):
        def to_representation(self, value):
            loan = {
                "id": value.id,
                "loan_date": value.loan_date,
                "devolution_date": value.devolution_date,
                "user_username": value.user.username,
            }
            return loan

    loans = LoanListingField(many=True, read_only=True)

    class Meta:
        model = BookCopy
        fields = ["id", "book", "added_on", "loans"]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "book": {"read_only": True},
            "added_on": {"read_only": True},
        }
