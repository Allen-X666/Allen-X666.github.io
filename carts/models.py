from django.db import models
from users.models import UserInfo
from products.models import Product

class Cart(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    user_id=models.ForeignKey('users.UserInfo',on_delete=models.CASCADE,related_name='carts1')
    product_id=models.ForeignKey('products.Product',on_delete=models.CASCADE,related_name='carts2')
    quantity=models.IntegerField(default=0,null=False)

    class Meta:
        db_table='carts'
        verbose_name='购物车表'
        verbose_name_plural=verbose_name
