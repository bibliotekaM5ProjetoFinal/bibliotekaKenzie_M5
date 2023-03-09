from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


@extend_schema_field(OpenApiTypes.OBJECT)
class FollowListingField(serializers.RelatedField):
    def to_representation(self, value):
        follow = {"title": value.book.title, "since": value.start_following}
        return follow


@extend_schema_field(OpenApiTypes.OBJECT)
class loansListingField(serializers.RelatedField):
    def to_representation(self, value):
        loan = {
            "id": value.id,
            "loan_date": value.loan_date,
            "devolution_date": value.devolution_date,
            "book_title": value.book_copy.book.title,
        }
        return loan


class UserSerializer(serializers.ModelSerializer):
    following = FollowListingField(read_only=True, many=True)
    loans = loansListingField(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "can_loan",
            "phone",
            "following",
            "loans",
        ]
        depth = 1
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="Email Alredy Registered",
                    )
                ],
                "required": True,
            },
        }

    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_superuser"):
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        return instance
