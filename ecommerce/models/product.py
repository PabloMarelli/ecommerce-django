from core.models import BaseModel
from django.db import models


class Product(BaseModel):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(null=True)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    seller_user = models.ForeignKey('ecommerce.Customer', null=True, on_delete=models.SET_NULL, related_name='seller_user')
    category = models.ForeignKey('ecommerce.Category', null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField('ecommerce.Tag')
    
    def __str__(self):
        return f'Id: {self.id} |Name: {self.name}|Active: {self.active}| Price: {self.price}'

    def save(self, *args, **kwargs):
        if self.seller_user.is_seller == False:
            self.seller_user.is_seller = True
            super(Product, self).save(*args, **kwargs)
        if self.quantity > 0 and self.active == False:
            self.active = True
        
        super(Product, self).save(*args, **kwargs)
