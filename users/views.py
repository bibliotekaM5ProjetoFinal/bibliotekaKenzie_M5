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


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffListingPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthOnlyPermission, StaffOrOwnerPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer
