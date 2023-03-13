from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.permissions import (
    AuthOnlyPermission,
    StaffListingPermission,
    StaffOrOwnerPermission,
    StaffPermission,
)
from users.serializers import UserSerializer
from drf_spectacular.utils import extend_schema


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffListingPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(methods=["PUT"], exclude=True)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthOnlyPermission, StaffOrOwnerPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer
