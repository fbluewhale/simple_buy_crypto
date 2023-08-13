from django.db import models
from utils.models import BaseModel


class Coin(BaseModel):
    name = models.CharField(max_length=50)
    abbreviation_name = models.CharField(max_length=20)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=18)
    sale_price = models.DecimalField(decimal_places=2, max_digits=18)

    def __str__(self) -> str:
        return f"{self.name}-{self.abbreviation_name}"
