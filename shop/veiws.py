from django.shortcuts import render, redirect
from django.urls import reverse

from carts.models import Cart
from users.models import UserInfor
from products.models import Product


#首页
def index(request):
    sessions=request.session.get('uid')
    products=Product.objects.all()
    content={
        'username':sessions,
        'products':products,
    }
    if sessions:
        return render(request,'index.html',context=content)
    else:
        return render(request,'index.html',{'products':products})

#注册页面
def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        uid=request.POST.get('uids')
        password=request.POST.get('passwords')
        repassword=request.POST.get('repasswords')
        uid_db=UserInfor.objects.filter(username2=uid)
        if uid_db:
            return render(request,'register.html',{'error':'用户名已存在'})
        else:
            if password == repassword:
                #password=sha256(password.encode('utf-8'))
                UserInfor.objects.create(id=uid,username2=uid,password2=password)
                return render(request,'login.html')
            else:
                return render(request,'register.html',{'error':'两次密码不一致'})

#登陆页面
def login(request):
    context = {
        'error': '用户名或密码错误',

    }
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        uid=request.POST.get('uid')
        password=request.POST.get('password')
        uid_db=UserInfor.objects.filter(username2=uid)
        password_db=UserInfor.objects.filter(password2=password)
        if uid_db and password_db:
            request.session['uid']=uid
            return redirect(reverse('index'))
        else:
            return render(request,'login.html',context=context)

#退出页面
def logout(request):
    request.session.flush()
    return redirect(reverse('index'))

#向carts里面添加商品
def add_to_cart(request):
    if before_login(request):
        if request.method == 'POST':
            uid = request.session.get('uid')
            pid = request.POST.get('pid')
            if not pid:  # 检查 pid 是否获取到
                print("未获取到商品 ID")
                return redirect(reverse('index'))  # 处理 pid 缺失的情况
            if uid:
                try:
                    carts = Cart.objects.filter(user_id=uid, product_id=pid)
                    if carts:
                        cart = carts[0]
                        cart.count += 1
                        cart.save()
                    else:
                        Cart.objects.create(id=1,user_id=uid, product_id=pid, quantity=1)
                except Exception as e:
                    print(f"添加商品到购物车时出错: {e}")  # 打印错误信息
        return redirect(reverse('carts:carts_list'))
    else:
        return redirect(reverse('login'))


#验证是否登录
def before_login(request):
    sessions=request.session.get('uid')
    if sessions:
        return True
    else:
        return False


