# -*- coding: UTF-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('user/list',views.user_list),
    path('chat-api/',views.chat_api),
    path('index/', views.index),
]