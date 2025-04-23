from django.db import models

class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    uname = models.CharField(max_length=50,unique=True,default='未填写')
    username1 = models.CharField(max_length=50,unique=True)
    password1 = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_info'
        verbose_name='用户'
        verbose_name_plural='用户信息'


class UserInfor(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    username2 = models.IntegerField(max_length=50,unique=True,null=False)
    password2 = models.IntegerField(max_length=50,null=False)

    class Meta:
        db_table = 'user_infor'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

