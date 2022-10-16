from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse
import json
from django.http import JsonResponse
import random


class UsersView(View):
    """用户视图"""

    data_return_dict = {
        'code': 0,
        'msg': None,
        'data': None,
    }

    def get(self, request):
        """
        获取全部用户
        @param request: object
        @return: JsonObject
        """
        data_users = {
            '1': {
                'id': 1,
                'username': 'zs',
                'name': '张三',
                'age': 18,
                'email': 'zhangsan@example.com'
            },
            '2': {
                'id': 2,
                'username': 'ls',
                'name': '李四',
                'age': 20,
                'email': 'lisi@example.com'
            },
        }
        self.data_return_dict.update(code=200, msg='successes', data=data_users)
        return JsonResponse(data=self.data_return_dict, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        """
        用户注册
        @param request: 
        @return: 
        """
        # form表单
        # users_username = self.request.POST.get('username')
        # users_password = self.request.POST.get('password')
        # users_name = self.request.POST.get('name')
        # users_age = self.request.POST.get('age')
        # users_email = self.request.POST.get('email')
        
        # json数据
        data_axios_users_str = self.request.body.decode('utf-8')
        data_axios_users_dict = json.loads(data_axios_users_str)
        users_username = data_axios_users_dict['username']
        users_password = data_axios_users_dict['password']
        users_name = data_axios_users_dict['name']
        users_age = data_axios_users_dict['age']
        users_email = data_axios_users_dict['email']
        
        users_data = {
            'id': random.randint(0, 100),
            'username': users_username,
            'name': users_name,
            'age': users_age,
            'email': users_email
        }
        print(users_password)
        self.data_return_dict.update(code=200, msg='successes', data=users_data)
        return JsonResponse(data=self.data_return_dict, json_dumps_params={'ensure_ascii': False})


class UserView(View):
    """用户视图"""

    data_return_dict = {
        'code': 0,
        'msg': None,
        'data': None,
    }

    def get(self, request, uid: str):
        """
        查询用户数据
        @param request: 
        @param uid: 用户id
        @return: 
        """
        if uid == '1':
            user_data = {
                'id': 1,
                'username': 'zs',
                'name': '张三',
                'age': 18,
                'email': 'zhangsan@example.com'
            }
            self.data_return_dict.update(code=200, msg='successes', data=user_data)
        else:
            self.data_return_dict.update(code=500, msg='error')
        return JsonResponse(data=self.data_return_dict, json_dumps_params={'ensure_ascii': False})

    def put(self, request, uid: str):
        """
        用户数据修改
        @param request: 
        @param uid: 
        @return: 
        """
        pass

    def delete(self, request, uid: str):
        """
        用户删除
        @param request: 
        @param uid: 
        @return: 
        """
        pass
