from core.models import BaseModel
from django.db import models

from django.conf import settings

class Customer(BaseModel):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Id: {self.id} |Name: {self.user.username} |Balance: {self.balance}'