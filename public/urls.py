# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/14 0:52
"""

import os, sys

from django.urls.conf import re_path
from public import views

urlpatterns = [
    re_path(r'', views.SignInView.as_view(), name='public')
]
