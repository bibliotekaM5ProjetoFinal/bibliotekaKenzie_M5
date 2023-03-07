from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class FollowListingField(serializers.RelatedField):
    def to_representation(self, value):
        follow = {"title": value.book.title, "since": value.start_following}
        return follow


class UserSerializer(serializers.ModelSerializer):
    following = FollowListingField(read_only=True, many=True)

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
