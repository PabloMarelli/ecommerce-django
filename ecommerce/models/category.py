from unicodedata import name
from core.models import BaseModel
from django.db import models


class Category(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    
    def __str__(self):
        return f'Id: {self.id} |Name: {self.name}'