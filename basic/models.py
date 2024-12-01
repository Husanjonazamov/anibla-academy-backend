from django.db import models
from botusers.models import BotUser


class ClickOrder(models.Model):
    is_paid = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
