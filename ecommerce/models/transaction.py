from core.models import BaseModel
from django.db import models
from ecommerce.models import Product

class Transaction(BaseModel):

    buyer_user = models.ForeignKey('ecommerce.Customer', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey('ecommerce.Product', null=True, on_delete=models.SET_NULL)   
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'Id: {self.id} |Product: {self.product.name} |Buyer: {self.buyer_user.user.username}'
    
    def save(self, *args, **kwargs):
        product = Product.objects.get(id=self.product.id)
        if self.buyer_user.balance >= (product.price * float(self.quantity)):
            if self.buyer_user.user.id != product.seller_user.user.id:
                if product.active == True:
                    product.quantity = product.quantity - self.quantity
                    if product.quantity > 0:
                        if self.buyer_user.is_buyer == False:
                            self.buyer_user.is_buyer = True
                            self.buyer_user.save()
                        self.buyer_user.balance = self.buyer_user.balance - (product.price * float(self.quantity))
                        self.buyer_user.save()
                        product.save()
                        super(Transaction, self).save(*args, **kwargs)
                    elif product.quantity == 0:
                        if self.buyer_user.is_buyer == False:
                            self.buyer_user.is_buyer = True
                            self.buyer_user.save()
                        self.buyer_user.balance = self.buyer_user.balance - (product.price * float(self.quantity))
                        self.buyer_user.save()
                        product.active = False
                        product.save()
                        super(Transaction, self).save(*args, **kwargs)
                    else:
                        raise Exception('Too many products')
                else:
                    raise Exception('Out of stock')
            else:
                raise Exception("Seller user can't buy his own products")
        else:
            raise Exception('Insuficient founds, please try again')