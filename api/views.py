from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from api.models import Payment
from api.serializators import PaymentSerializer


class PaymentViewSet(APIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentList(generics.ListAPIView):
    authentication_classes = (SessionAuthentication,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all().order_by('-id')