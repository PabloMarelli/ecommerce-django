from core.models import BaseModel
from django.db import models


class Tag(BaseModel):

    name =  models.CharField(max_length=200)
         
    def __str__(self):
        return f'Id: {self.id} |Name: {self.name}'