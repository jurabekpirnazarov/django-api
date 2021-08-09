from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Reminder(models.Model):
    NameCompany = models.CharField(max_length=500)
    ID_gruppa = models.CharField(max_length=20)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.NameCompany
