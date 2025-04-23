from django.contrib import admin
from django.urls import path, include
from .veiws import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('register/', register,name='register'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('add_to_cart/', add_to_cart,name='add_to_cart'),
    path('user/',include('users.uurls',namespace='users')),
    path('products/',include('products.purls',namespace='products')),
    path('carts/',include('carts.curls',namespace='carts')),
]

