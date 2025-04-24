from django.shortcuts import render, redirect
from users.models import *
def user_center(request):
    username = request.session.get('uid')
    user = None
    if username:
        try:
            user = UserInfo.objects.get(username1=username)
        except UserInfo.DoesNotExist:
            request.session.flush()
            return redirect('login')
    context = {
        'username': username,
        'user': user,
    }
    return render(request, 'user_center.html', context=context)


