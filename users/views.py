from django.shortcuts import render

def user_center(request):
    username=request.session.get('uid')
    context={
        'username':username,
    }
    if username:
        return render(request,'user_center.html',context=context)
    else:
        return render(request,'user_center.html')


