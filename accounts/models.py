from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    id_telegram = models.CharField(max_length=150)
    url_bit = models.CharField(max_length=150)
    data_time = models.CharField(max_length=150)
