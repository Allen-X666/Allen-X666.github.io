from django.db import models
from users.models import UserInfo

class Order(models.Model):
    PENDING = 1
    PAID = 2
    SHIPPED = 3
    COMPLETED = 4

    ORDER_STATUS_CHOICES = [
        (PENDING, '待支付'),
        (PAID, '已支付'),
        (SHIPPED, '已发货'),
        (COMPLETED, '已完成'),
    ]
    id=models.IntegerField(primary_key=True,auto_created=True)
    user_id=models.ForeignKey('users.UserInfo',on_delete=models.CASCADE,related_name='user_id1')
    order_date=models.DateField(auto_now=False,auto_now_add=False)
    status=models.IntegerField(choices=ORDER_STATUS_CHOICES,default=PENDING)#默认为待支付

    class Meta:
        db_table='orders'
        verbose_name='订单表'
        verbose_name_plural=verbose_name
