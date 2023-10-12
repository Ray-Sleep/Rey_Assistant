# -*- coding: UTF-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login),
    path('user/list',views.user_list),
    path('chat-api/',views.chat_api),
    path('', views.index),
]