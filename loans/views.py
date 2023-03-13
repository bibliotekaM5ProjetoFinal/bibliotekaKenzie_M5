from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from books.models import BookCopy
from users.models import User
from users.permissions import StaffPermission
from .models import Loan
from .serializers import LoanSerializer
from datetime import datetime, timedelta
from drf_spectacular.utils import extend_schema
import ipdb

# Create your views here.


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffPermission]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.validated_data["user"]
        book_copy: BookCopy = serializer.validated_data["book_copy"]

        # :: Checagens por cópia ::
        for loan in Loan.objects.filter(book_copy=book_copy):
            # se a cópia do livro já está emprestada a um usuário
            if loan.devolution_date is None:
                return Response(
                    {"detail": "This copy is already loaned"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # :: Checagens por usuário ::
        if not user.can_loan:
            return Response(
                {"detail": "The user is blocked and can not make new loans"}, 
                status=status.HTTP_403_FORBIDDEN
            )

        serializer.save(
            user=user, 
            book_copy=book_copy
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(methods=["PUT"], exclude=True)
class LoanDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffPermission]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "loan_pk"
