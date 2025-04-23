from django.shortcuts import render, redirect
from django.urls import reverse

from products.models import Product
from users.models import UserInfor


#购物车
def cart(request):
    if before_login(request):
        username=request.session.get('uid')
        pros=Product.objects.get(id=1)
        print(pros.price)
        context = {
            'username':username,
            'pros':pros,
        }
        return render(request,'carts.html',context=context)
    else:
        return redirect(reverse('login'))



#钩子函数，检验是否登陆
def before_login(request):
    sessions=request.session.get('uid')
    if sessions:
        return True
    else:
        return False
