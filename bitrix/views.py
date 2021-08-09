from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Bitrix
from .serializer import BitrixSerializer
# Create your views here.

class BitrixList(ListCreateAPIView):
    queryset = Bitrix.objects.all()
    serializer_class = BitrixSerializer

class BitrixDetail(RetrieveUpdateDestroyAPIView):
    queryset = Bitrix.objects.all()
    serializer_class = BitrixSerializer