from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('NameCompany',"ID_gruppa", 'date',)
        model = Reminder