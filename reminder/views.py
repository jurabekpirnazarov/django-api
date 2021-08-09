from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Reminder
from .serializer import ReminderSerializer
# Create your views here.

class RemainderList(ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class RemainderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer