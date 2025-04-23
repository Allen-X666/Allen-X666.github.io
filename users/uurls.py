from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('user_center/', user_center,name='user_center'),
]