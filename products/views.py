from django.shortcuts import render, redirect
from products.models import Product
from users.models import UserInfo,UserInfor



def products_list(request):
    products = Product.objects.all()
    username = request.session.get('uid')
    user = None
    if username:
        try:
            user = UserInfo.objects.get(username1=username)
        except UserInfo.DoesNotExist:
            request.session.flush()
            return redirect('login')
    content = {
        'products': products,
        'username': username,
        'user': user,
    }
    return render(request, 'products_list.html', context=content)
