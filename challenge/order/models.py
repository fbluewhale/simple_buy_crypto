from django.db import models
from utils.models import BaseModel
from account.models import UserProfile
from coin.models import Coin

# Create your models here.


class Order(BaseModel):
    user = models.ForeignKey(
        UserProfile, related_name="account", on_delete=models.PROTECT
    )
    coin = models.ForeignKey(Coin, related_name="coin", on_delete=models.PROTECT)
    purchase_price = models.DecimalField(
        "Crypto purchase price", decimal_places=2, max_digits=18
    )
    sale_price = models.DecimalField(
        "Crypto sales price", decimal_places=2, max_digits=18, default=0
    )
    total_price = models.DecimalField(
        "order total price", decimal_places=2, max_digits=18
    )

    external_checkout = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2, max_digits=18)

    def __str__(self):
        return f"{self.user.user.username}-{self.coin.abbreviation_name}- amount: {self.amount} - total price : {self.total_price}"
