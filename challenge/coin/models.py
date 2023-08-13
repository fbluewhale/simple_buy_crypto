from django.db import models
from utils.models import BaseModel


class Coin(BaseModel):
    name = models.CharField(max_length=50)
    abbreviation_name = models.CharField(max_length=20)
    purchase_price = models.DecimalField()
    sale_price = models.DecimalField()

    def __str__(self) -> str:
        return f"{self.name}-{self.abbreviation_name}"
