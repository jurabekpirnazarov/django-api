from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bitrix(models.Model):
    id_telegram = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=14)
    url_bitrix = models.CharField(max_length=500)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.id_telegram
