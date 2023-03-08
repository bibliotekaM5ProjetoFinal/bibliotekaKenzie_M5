from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import Response
from .models import Loan
from users.models import User
from books.models import BookCopy
from .serializers import LoanSerializer
from datetime import datetime, timedelta
import ipdb
from django.shortcuts import get_object_or_404

# Create your views here.


class LoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        book_copy = serializer.validated_data["book_copy"]

        # :: Checagens por cópia ::
        for loan in Loan.objects.filter(book_copy=book_copy):
            # se a cópia do livro já está emprestada a um usuário
            if loan.devolution_date is None:
                return Response(
                    {"detail": "This copy is already loaned"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # :: Checagens por usuário ::
        for loan in Loan.objects.filter(user=user):
            today_date = datetime.now().date()
            expiration_date = loan.loan_date + timedelta(days=7)
            # se o usuário ainda não entregou uma cópia pendente.
            if loan.devolution_date is None and today_date > expiration_date:
                return Response(
                    {"detail": "The user has not returned expired loans"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            # se o usuário entregou a cópia, porém, fora do prazo
            if loan.devolution_date:
                if loan.devolution_date > expiration_date:
                    block_date = loan.devolution_date + timedelta(days=2)
                    if today_date < block_date:
                        return Response(
                            {
                                "detail": "The user is temporarily blocked from making loans"
                            },
                            status=status.HTTP_403_FORBIDDEN,
                        )

        serializer.save(user=user, book_copy=book_copy)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoanDetailView(generics.RetrieveUpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "loan_pk"
