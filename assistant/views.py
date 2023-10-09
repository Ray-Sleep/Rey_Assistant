import re
from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .openai_key import key
import requests
import openai

import json


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
    elif not re.match(r"^1[3-9]\d{9}$", number):
        return HttpResponse('注册失败，请输入正确的手机号')
    else:
        UserInfo.objects.create(name=username, number=number, password=password)
        return render(req, 'index.html')

    # 登入
    """检测用户名、邮箱、电话 是否存在数据库"""
    if number == '':
        pass

    # if username == 'admin' and password == '123':
    #     return HttpResponse('登录成功')
    return render(req,'index.html')


def index(request):
    return render(request,'index.html')


def user_list(req):
    # 获取所有用户信息
    user_data = UserInfo.objects.all()
    return render(req, 'user_list.html', {'data_list': user_data})


@api_view(['GET', 'POST'])
def chat_api(request):
    openai_secret_key = key
    # 设置对话内容
    message = []
    while True:
        # 输入对话当前关键词
        content = input("User: ")
        # 向对话内容
        message.append({"role": "user", "content": content})
        # 调用api
        completion = openai.ChatCompletion.create(
            api_key=openai_secret_key,
            model="gpt-3.5-turbo",
            messages=message
        )
        # 获取回复
        chat_response = completion
        answer = chat_response.choices[0].message.content
        # 打印回复
        print(f'ChatGPT: {answer}')
        # 向对话内容添加回复
        message.append({"role": "assistant", "content": answer})
        # 打印历史记录
        print(message)