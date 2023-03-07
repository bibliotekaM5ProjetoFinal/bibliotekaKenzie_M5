from rest_framework import serializers
from .models import Book, BookCopy
from rest_framework.response import Response


class FollowedListingField(serializers.RelatedField):
    def to_representation(self, value):
        follow = {"email": value.user.email, "since": value.start_following}
        return follow


class BookSerializer(serializers.ModelSerializer):
    followed_by = FollowedListingField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "synopsis", "copies", "followed_by"]
        depth = 1
        extra_kwargs = {"id": {"read_only": True}}


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ["id", "book", "added_on"]
        depth = 1
        extra_kwargs = {
            "id": {"read_only": True},
            "book": {"read_only": True},
            "added_on": {"read_only": True},
        }
