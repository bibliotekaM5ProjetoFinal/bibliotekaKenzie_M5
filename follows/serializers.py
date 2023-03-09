from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Follow
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.EMAIL)
    def get_user(self, obj):
        return obj.user.email

    @extend_schema_field(OpenApiTypes.STR)
    def get_book(self, obj):
        return obj.book.title

    class Meta:
        model = Follow
        fields = ["id", "start_following", "user", "book"]

    # def create(self, validated_data: dict) -> Follow:
    #     return Follow.objects.create(**validated_data)
