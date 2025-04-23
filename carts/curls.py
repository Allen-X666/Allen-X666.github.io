from django.urls import path
from .views import *


app_name = 'carts'

urlpatterns = [
    path('carts_list/', cart, name='carts_list'),
]
