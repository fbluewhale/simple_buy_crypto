from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.


class User(DjangoUser):
    balance = models.BigIntegerField(default=0)
