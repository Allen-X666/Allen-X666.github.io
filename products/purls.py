from django.urls import path
from .views import *


app_name = 'products'

urlpatterns = [
    path('products_list/', products_list, name='products_list'),
]

