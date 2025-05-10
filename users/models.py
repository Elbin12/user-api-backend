from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=200)
    age = models.PositiveBigIntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    web = models.URLField()