from rest_framework import serializers
from .models import Bitrix

class BitrixSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id_telegram", 'phone_number', 'url_bitrix', 'date',)
        model = Bitrix