from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status
from books.models import Book
from users.models import User
from users.permissions import AuthOnlyPermission, StaffOrOwnerPermission, TestPermission
from .models import Follow
from rest_framework.views import Response


from follows.serializers import FollowSerializer

# Create your views here.


class FollowView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthOnlyPermission]

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)
        book = get_object_or_404(Book, id=self.request.data.get("bookId"))
        serializer.save(user=user, book=book)


class FollowDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthOnlyPermission, StaffOrOwnerPermission]

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    lookup_url_kwarg = "pk"

    def retrieve(self, request, *args, **kwargs):
        follow = get_list_or_404(Follow, user=self.kwargs.get("pk"))
        user = get_object_or_404(User, id=self.kwargs.get("pk"))

        self.check_object_permissions(request, user)
        print(self.check_object_permissions(request, user))
        serializer = self.get_serializer(follow, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        follow = get_object_or_404(Follow, id=self.kwargs.get("pk"))
        user = get_object_or_404(User, following=self.kwargs.get("pk"))
        self.check_object_permissions(request, user)

        self.perform_destroy(follow)
        return Response(status=status.HTTP_204_NO_CONTENT)
