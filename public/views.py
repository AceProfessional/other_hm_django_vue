from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse
import json


class SignInView(View):
    
    def get(self, request):
        self.request.GET.get('user')
        # ss = self.request.body.decode('utf-8')
        ss = json.loads(self.request.body.decode('utf-8'))
        print(ss)
        return HttpResponse('ok')