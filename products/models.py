from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    description = models.TextField(default='暂无商品描述')
    stock = models.IntegerField(default=0)#库存
    image = models.ImageField(upload_to='products/',default='products/default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name='商品'
        verbose_name_plural=verbose_name