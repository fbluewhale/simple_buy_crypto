from django.db import models
from django.contrib.auth.models import User as DjangoUser

from utils.models import BaseModel

# Create your models here.


class UserProfile(BaseModel):
    user = models.OneToOneField(
        DjangoUser, related_name="Account", on_delete=models.PROTECT
    )
    balance = models.BigIntegerField(default=0)
