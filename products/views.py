from django.shortcuts import render
from products.models import Product




def products_list(request):
    products=Product.objects.all()
    username=request.session.get('uid')
    content={
        'products':products,
        'username':username,
    }
    if username:
        return render(request,'products_list.html',context=content)
    else:
        return render(request,'products_list.html',{'products':products})
