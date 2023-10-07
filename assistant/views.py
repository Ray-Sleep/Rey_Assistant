import re
from django.shortcuts import render,HttpResponse,redirect
from .models import UserInfo


def login(req):
    print(req.POST)

    if req.method == 'GET':
        return render(req, 'user_login.html')

    username = req.POST.get('user')
    number = req.POST.get('number')
    password = req.POST.get('pwd')

    # 注册
    """
    检测用户名、邮箱、电话是否重复
    """
    if UserInfo.objects.filter(name=username).exists() and UserInfo.objects.filter(number=number).exists():
        return HttpResponse('注册失败，用户名或手机号重复')
    elif not re.match(r"^1[3-9]\d{9}$",number):
        return HttpResponse('注册失败，请输入正确的手机号')
    else:
        UserInfo.objects.create(name=username, number=number, password=password)
        return render(req, 'user_list.html')

    # 登入
    """检测用户名、邮箱、电话 是否存在数据库"""
    if number == '':
        pass

    # if username == 'admin' and password == '123':
    #     return HttpResponse('登录成功')
    return HttpResponse('登录成功')



def user_list(req):
    # 获取所有用户信息
    user_list = UserInfo.objects.all()
    return render(req, 'user_list.html', {'data_list': user_list})